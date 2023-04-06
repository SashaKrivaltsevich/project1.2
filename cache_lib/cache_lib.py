from typing import Dict, Tuple, Union
from time import time


class SimpleCache:
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            key = tuple(args), tuple(sorted(kwargs.items()))
            if key not in self.cache:
                self.cache[key] = func(*args, **kwargs)
            return self.cache[key]

        return wrapper


class FIFOCache:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.cache = {}
        self.keys = []

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            key = tuple(args), tuple(sorted(kwargs.items()))
            if key not in self.cache:
                if len(self.cache) >= self.max_size:
                    del self.cache[self.keys.pop(0)]
                self.cache[key] = func(*args, **kwargs)
                self.keys.append(key)
            return self.cache[key]

        return wrapper


class LRUCache:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.cache = {}
        self.keys = []

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            key = tuple(args), tuple(sorted(kwargs.items()))
            if key in self.cache:
                self.keys.remove(key)
            elif len(self.cache) >= self.max_size:
                old_key = self.keys.pop(0)
                del self.cache[old_key]
            self.cache[key] = func(*args, **kwargs)
            self.keys.append(key)
            return self.cache[key]

        return wrapper


class TTLCache:
    def __init__(self, max_size: int, ttl: int):
        self.max_size = max_size
        self.ttl = ttl
        self.cache: Dict[Tuple, Tuple[float, Union[bytes, None]]] = {}

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # Create a tuple from positional and keyword arguments to use as a key for caching
            key = tuple(args), tuple(sorted(kwargs.items()))
            # Get the current time
            current_time = time.time()

            # if the key is in the cache, check if the cached value is valid
            if key in self.cache:
                last_accessed, value = self.cache[key]
                # If the cached value is ended, delete it from the cache and set value to None
                if current_time - last_accessed > self.ttl:
                    del self.cache[key]
                    value = None
            else:
                # If the key is not in the cache, set value to None
                # and check if the cache is full
                if len(self.cache) >= self.max_size:
                    # If the cache is full, find the oldest cache and delete it from the cache
                    for k, (ts, _) in sorted(self.cache.items(), key=lambda x: x[1][0]):
                        if current_time - ts > self.ttl:
                            del self.cache[k]
                            break
                value = None

            # If value is still None, call the wrapped function to calculate the result
            # and store the result in the cache
            if value is None:
                value = func(*args, **kwargs)
                self.cache[key] = (current_time, value)
            return value

        return wrapper
