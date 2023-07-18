#!/usr/bin/env python3
""" List pymongo"""
import pymongo


def list_all(mongo_collection):
    """List all documents"""
    documents = list(mongo_collection.find({}))
    return documents
