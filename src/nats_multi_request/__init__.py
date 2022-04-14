import asyncio
import sys
from asyncio import Future
from typing import Any, Union

from nats.aio.client import Client as NATSClient
from nats.aio.msg import Msg
from nats.aio.errors import ErrTimeout

if sys.version_info >= (3, 9):
    List = list
else:
    from typing import List


async def wait_for_responses(
    nats_conn: NATSClient, subject: str, payload: bytes, timeout: float, expected: int
) -> List[Msg]:
    responses = []

    # Convert asyncio.sleep() into a future so we can cancel it.
    sleep_timeout: Future[Any] = asyncio.ensure_future(asyncio.sleep(timeout))

    async def add_to_list(msg: Msg):
        responses.append(msg)
        if len(responses) == expected:
            sleep_timeout.cancel()

    reply_subject = nats_conn.new_inbox()

    await nats_conn.publish(subject, payload, reply=reply_subject)

    subscription = await nats_conn.subscribe(
        subject=reply_subject,
        cb=add_to_list,
    )

    try:
        await sleep_timeout
    except asyncio.CancelledError:
        pass

    await subscription.unsubscribe()
    return responses


async def request(
    nats_conn: NATSClient,
    subject: str,
    payload: bytes,
    error_if_lt_expected: bool = False,
    timeout: float = 0.5,
    expected: int = 1,
) -> Union[Msg, List[Msg]]:
    """Make a request to NATS. Return response as soon as it arrives. If
    expected > 1, return multiple responses.

    :param subject: NATS subject
    :param payload: NATS payload, should be bytes
    :param error_if_lt_expected: Raise error is less than `expected` responses \
        received. Converted to boolean
    :param timeout: Time to wait for `expected` responses.
    :param expected: Expected number of messages.

    :returns: Msg if expected == 1
    :returns: List[Msg] if expected > 1

    :raises nats.aio.errors.ErrTimeout: if no responses received or if \
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
