#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Prints stats about Nginx logs."""
    print("{} logs".format(mongo_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    status_count = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status_count))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_stats(client.logs.nginx)
