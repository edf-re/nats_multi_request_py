import asyncio
import sys
from asyncio import Queue
from typing import Union

from nats.aio.client import Client as NATSClient
from nats.aio.client import Msg
from nats.aio.errors import ErrTimeout

if sys.version_info >= (3, 9):
    from collections.abc import Awaitable

    List = list
else:
    from typing import Awaitable, List


async def wait_for_responses(
    nats_conn, subject, payload, timeout, expected
) -> List[Msg]:
    responses = []

    # Use this queue as a cancel-able async sleep.
    # When add_to_list adds an element to it, stop sleeping.
    wait_queue: Queue[str] = Queue()

    def add_to_list(msg: Msg):
        responses.append(msg)
        if len(responses) == expected:
            wait_queue.put_nowait("done")

    sid = await nats_conn.request(
        subject,
        payload,
        timeout=timeout,
        expected=expected,
        cb=add_to_list,
    )

    # Sleep
    try:
        await asyncio.wait_for(wait_queue.get(), timeout)
    except asyncio.TimeoutError:
        pass

    await nats_conn.unsubscribe(sid)
    return responses


async def request(
    nats_conn: NATSClient,
    subject: str,
    payload: bytes,
    error_if_lt_expected=False,
    timeout=0.5,
    expected=1,
) -> Union[Msg, List[Msg]]:
    """Make a request to NATS. Return response as soon as it arrives. If
    expected > 1, return multiple responses.

    subject - NATS subject
    payload - NATS payload, should be bytes
    error_if_lt_expected - Raise error is less than `expected` responses
        received. Converted to boolean
    timeout - Time to wait for `expected` responses.
    expected - Expected number of messages.

    returns:
    Msg - if expected == 1
    List[Msg] - if expected > 1

    raises nats.aio.errors.ErrTimeout if no responses received or if
    error_if_lt_expected is True and less than expected responses received.
    """
    error_if_lt_expected = bool(error_if_lt_expected)
    assert int(expected) == expected, "expected must be int"
    assert expected > 0, "expected must be greater than 0"

    responses = await wait_for_responses(nats_conn, subject, payload, timeout, expected)

    if len(responses) == 0 or (len(responses) < expected and error_if_lt_expected):
        raise ErrTimeout

    if expected == 1:
        return responses[0]
    return responses
