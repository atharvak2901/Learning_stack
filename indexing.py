"""
ndexing in MongoDB is a crucial performance optimization technique that allows for faster data retrieval. It works similarly to an index in a book, which helps you quickly find the pages related to a particular topic without having to read the entire book.

What is an Index?
In MongoDB, an index is a data structure that improves the speed of data retrieval operations on a database collection. It essentially creates a sorted structure of the indexed field(s) which MongoDB can use to quickly locate the documents that match a query. Without an index, MongoDB must perform a collection scan, examining each document to find matches, which can be slow for large collections.

Example
Let's walk through a simple example to illustrate how indexing works in MongoDB.

1. Sample Data

Imagine you have a MongoDB collection named users with the following documents:

json
Copy code
{ "_id": 1, "name": "Alice", "age": 25 }
{ "_id": 2, "name": "Bob", "age": 30 }
{ "_id": 3, "name": "Charlie", "age": 35 }
{ "_id": 4, "name": "David", "age": 25 }
You frequently query this collection based on the age field. For example:

javascript
Copy code
db.users.find({ age: 25 });
2. Without Index

Without an index on the age field, MongoDB will perform a collection scan. This means MongoDB will go through each document in the users collection and check if the age field matches the query value (25). If the collection is large, this process can be slow.

3. Creating an Index

To improve performance, you can create an index on the age field. Here’s how you can do it:

javascript
Copy code
db.users.createIndex({ age: 1 });
The { age: 1 } part specifies that you want to create an ascending index on the age field. (You can use -1 for a descending index if needed.)

4. How Indexing Improves Performance

Once the index is created, MongoDB builds a data structure (a B-tree) that maintains the age values in sorted order. When you run the query db.users.find({ age: 25 }), MongoDB can use this index to quickly locate the documents where age is 25 without scanning the entire collection. It finds the index entry corresponding to 25, and then retrieves the documents associated with that entry.

5. Checking the Index

To see the indexes on your collection, you can use:

javascript
Copy code
db.users.getIndexes();
This command will list all indexes, including the one you just created on the age field.

Summary
Index: A data structure that speeds up data retrieval operations.
Without Index: MongoDB scans the entire collection to find matching documents.
With Index: MongoDB uses the index to quickly locate matching documents, significantly improving query performance.
By indexing fields that are frequently queried, you can greatly improve the efficiency of your database operations.




Time-To-Live (TTL) is a feature in MongoDB that allows you to automatically remove documents from a collection after a specified period of time. This is particularly useful for managing data that is only relevant for a limited time, such as session data, logs, or temporary files.

How TTL Works
TTL Index: You create a TTL index on a date field. MongoDB uses this index to track the expiration time of each document.
Automatic Deletion: MongoDB automatically removes documents that have passed their expiration time based on the TTL index.
Example: Expiring Session Data
Let's say you are building a web application and you want to manage user sessions. You want to store session data in MongoDB but automatically remove session records that haven't been accessed in the last 30 minutes.

1. Collection Schema

You have a sessions collection with documents structured like this:

json
Copy code
{ "_id": "sessionId1", "userId": "user123", "lastAccessed": ISODate("2024-09-05T10:00:00Z") }
{ "_id": "sessionId2", "userId": "user456", "lastAccessed": ISODate("2024-09-05T10:15:00Z") }
_id: A unique identifier for the session.
userId: The ID of the user.
lastAccessed: The timestamp of the last time the session was accessed.
2. Creating a TTL Index

You want to automatically remove sessions that haven't been accessed in the last 30 minutes. To achieve this, you create a TTL index on the lastAccessed field.

javascript
Copy code
db.sessions.createIndex({ lastAccessed: 1 }, { expireAfterSeconds: 1800 });
Here’s what’s happening:

{ lastAccessed: 1 }: Specifies that the index is on the lastAccessed field, in ascending order.
{ expireAfterSeconds: 1800 }: Sets the TTL to 1800 seconds (30 minutes). Documents where lastAccessed is older than 30 minutes from the current time will be automatically removed.
3. How It Works

Index Maintenance: MongoDB uses the TTL index to periodically check documents and compare the lastAccessed value with the current time.
Document Removal: When the TTL expires for a document (i.e., lastAccessed is older than 30 minutes), MongoDB will automatically remove the document from the collection.
4. Benefits

Automatic Cleanup: TTL indexes help manage data lifecycle automatically, ensuring old or irrelevant data is removed without manual intervention.
Reduced Storage Costs: By removing outdated documents, you can reduce storage costs and maintain optimal performance.

"""

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]
collection = db["test_collection"]

collection.find({"id":"1"}).explain()["executionStats"]

