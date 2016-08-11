AsyncIO

PEP 3156
https://www.python.org/dev/peps/pep-3156/


- Common way to do async tasks is to use threads.
    - expensive, context switching
- Async way is to use a single thread using an event loop
    - Wait for task
    - Perform operation
    - Call callback

Resources:
http://sahandsaba.com/understanding-asyncio-node-js-python-3-4.html