# Probe 3 crashed

```
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/urllib3/connection.py", line 239, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/socket.py", line 978, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno -5] No address associated with hostname

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 793, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 494, in _make_request
    raise new_e
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 470, in _make_request
    self._validate_conn(conn)
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 1125, in _validate_conn
    conn.connect()
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/urllib3/connection.py", line 827, in connect
    self.sock = sock = self._new_conn()
                       ^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/urllib3/connection.py", line 246, in _new_conn
    raise NameResolutionError(self.host, self, e) from e
urllib3.exceptions.NameResolutionError: HTTPSConnection(host='quote-api.jup.ag', port=443): Failed to resolve 'quote-api.jup.ag' ([Errno -5] No address associated with hostname)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/urllib3/connectionpool.py", line 847, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/urllib3/util/retry.py", line 555, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='quote-api.jup.ag', port=443): Max retries exceeded with url: /v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqzSqLzh7JKwqjVwtJpTsxNw9dSLE6Dt1v&amount=100000000&slippageBps=500 (Caused by NameResolutionError("HTTPSConnection(host='quote-api.jup.ag', port=443): Failed to resolve 'quote-api.jup.ag' ([Errno -5] No address associated with hostname)"))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/memecoin-trader/memecoin-trader/code/research/probe_jup.py", line 91, in <module>
    main()
  File "/home/runner/work/memecoin-trader/memecoin-trader/code/research/probe_jup.py", line 48, in main
    sc, js = quote(h, SOL, "EPjFWdd5AufqzSqLzh7JKwqjVwtJpTsxNw9dSLE6Dt1v", 1e8)   # SOL->USDC sanity check
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/memecoin-trader/memecoin-trader/code/research/probe_jup.py", line 32, in quote
    r = requests.get(host, params={"inputMint": inp, "outputMint": outp, "amount": int(amount), "slippageBps": 500},
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.15/x64/lib/python3.12/site-packages/requests/adapters.py", line 700, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='quote-api.jup.ag', port=443): Max retries exceeded with url: /v6/quote?inputMint=So11111111111111111111111111111111111111112&outputMint=EPjFWdd5AufqzSqLzh7JKwqjVwtJpTsxNw9dSLE6Dt1v&amount=100000000&slippageBps=500 (Caused by NameResolutionError("HTTPSConnection(host='quote-api.jup.ag', port=443): Failed to resolve 'quote-api.jup.ag' ([Errno -5] No address associated with hostname)"))

```
