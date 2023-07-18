#!/usr/bin/env python3
"""MongoDB storage"""
from pymongo import MongoClient


def log_stats():
    """check for elements in  collection"""
    client = MongoClient('mongodb://localhost:27017')

    db = client['logs']
    collection = db['nginx']

    num_logs = collection.count_documents({})
    print(f"{num_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    client.close()


if __name__ == "__main__":
    log_stats()
