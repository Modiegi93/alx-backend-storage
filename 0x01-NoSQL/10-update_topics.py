#!/usr/bin/env python3
"""pymongo list"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document"""
    query = {'name': name}
    update = {'$set': {'topics': topics}}
    mongo_collection.update_many(query, update)
