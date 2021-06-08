# nats_request_asap

[![Documentation Status](https://readthedocs.org/projects/nats-request-asap/badge/?version=latest)](https://nats-request-asap.readthedocs.io/en/latest/?badge=latest)

Python function to return one or multiple responses to a NATS request as soon as possible.

## Documentation

[nats-request-asap.readthedocs.io](https://nats-request-asap.readthedocs.io/)

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

## License

This project is under the MIT License. See [LICENSE.txt](./LICENSE.txt).
