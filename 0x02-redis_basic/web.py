#!/usr/bin/env python3
"""Get a web page"""
import redis
import requests
from typing import Callable
from functools import wraps


r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Decorator for counting """
    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator """
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Get the html content of a url"""
    req = requests.get(url)
    return req.text
