#!/usr/bin/env python3
"""Get a web page"""
import redis
import requests
from typing import Union


def get_page(url: str) -> str:
    """Track a number of times a particular URL was accessed"""
    r = redis.Redis()

    count_key = f"count:{url}"
    cached_content_key = f"content:{url}"

    count = r.get(count_key)
    if count is None:
        count = 1
    else:
        count = int(count) + 1

    content = r.get(cached_content_key)
    if content is None:
        response = requests.get(url)
        content = response.text

        r.setex(cached_content_key, 10, content)

    r.setex(count_key, 10, count)

    return content

if __name__ == "__main__":
    url = ('http://slowwly.robertomurray.co.uk')
    page_content = get_page(url)
    print(page_content)
