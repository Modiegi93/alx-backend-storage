#!/usr/bin/env python3
"""MongoDB storage"""
from pymongo import MongoClient


if __name__ == "__main__":
    """check for elements in  collection"""
    client = MongoClient('mongodb://localhost:27017')
    collection = client.logs.nginx

    print(f"{collection.estimated_document_count()} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    print("IPs:")
    pipeline = [
            {
                '$group': {
                    '_id': '$ip',
                    'count': {'$sum': 1}
                }
            },
            {
                '$sort': {
                    'count': -1
                }
            },
            {
                '$limit': 10
            }
    ]
    result = collection.aggregate(pipeline)
    for doc in result:
        print(f"\t{doc['_id']}: {doc['count']}")
