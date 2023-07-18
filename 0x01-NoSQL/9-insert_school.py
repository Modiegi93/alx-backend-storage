#!/usr/bin/env python3
""" pymongo lists"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document"""
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    new_id = result.inserted_id
    return new_id
