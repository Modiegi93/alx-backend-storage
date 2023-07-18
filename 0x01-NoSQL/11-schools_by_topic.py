#!/usr/bin/env python3
"""pymongo lists"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school with a specific topic"""
    query = {'topics': topic}
    schools = list(mongo_collection.find(query))
    return schools
