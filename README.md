# nats_request_asap

Python function to return one or multiple responses to a NATS request as soon as possible.

## Installation

```
pip install nats_request_asap
```

## Usage

### One response

Return a single NATS `Msg`.

```
>>> import nats_request_asap
>>> nats_request_asap.req_asap(z, b'{"nodes": ["af9c"]}', timeout=5)
<Msg: subject='_INBOX.tdSY0nNLoa9bYPqw9moCwC' reply='' data='{"initial_...'>
```

### Multiple responses

Return a list of NATS `Msg`s.

```
>>> nats_request_asap.req_asap(z, b'{"nodes": "all"}', expected=3, timeout=5)
[<Msg: subject='_INBOX.tdSY0nNLoa9bmNqw9moCwC' reply='' data='{"error": ...'>,
 <Msg: subject='_INBOX.tdSY0nNLoa9bmNqw9moCwC' reply='' data='{"initial_...'>,
 <Msg: subject='_INBOX.tdSY0nNLoa9bmNqw9moCwC' reply='' data='{"initial_...'>]
```
