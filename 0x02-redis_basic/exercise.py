#!/usr/bin/env python3
""" Cache with Redis"""
import redis
import uuid
import functools
from typing import Union, Callable


def call_history(method: Callable) -> Callable:
    """Returns a Callable"""
    key_inputs = method.__qualname__ + ":inputs"
    key_outputs = method.__qualname__ + ":outputs"

    @functools.wraps(method)
    def wrapped(self, *args, **kwargs):
        """Store the input in Redis"""
        self._redis.rpush(key_inputs, str(args))

        """Call the original method and store output"""
        output = method(self, *args, **kwargs)
        self._redis.rpush(key_outputs, str(output))

        return output
    return wrapped

def count_calls(method: Callable) -> Callable:
        """ Returns a Callable"""
        key = method.__qualname__

        @functools.wraps(method)
        def wrapped(self, *args, **kwargs):
            """Accesses the Redis instance"""
            self._redis.incr(key)
            return method(self, *args, **kwargs)

        return wrapped

class Cache:
    """Cache class"""
    def __init__(self):
        """Initializing class"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method to store"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
        """Convert data back to desired format"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """Convert to string"""
        return self.get(key, fn=lambda d: d.decode("utf-8") if d else None)

    def get_int(self, key: str) -> Union[int, None]:
        """Convert to int"""
        return self.get(key, fn=int) if self._redis.get(key) is not None else None

def replay(method: Callable):
    """Display the history of calls"""
    key_inputs = method.__qualname__ + ":inputs"
    key_outputs = method.__qualname__ + ":outputs"

    inputs = [eval(input_str) for input_str in cache._redis.lrange(key_inputs, 0, -1)]
    outputs = cache._redis.lrange(key_outputs, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}{str(inp)} -> {out.decode()}")


if __name__ == "__main__":
    cache = Cache()

    cache
