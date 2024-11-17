from pymongo import MongoClient
from pymongo.errors import ConnectionFailure



class MongoOperation:
    def __init__(self, connection_string):
        """
        Initialize the MongoDB client and connect to the database.
        :param connection_string: MongoDB connection URI
        """
        try:
            self.client = MongoClient(connection_string)
            # Test the connection
            self.client.admin.command('ping')
            print("Successfully connected to MongoDB!")
        except ConnectionFailure as e:
            raise Exception(f"Failed to connect to MongoDB: {e}")

    def get_database(self, db_name):
        """
        Get a database instance.
        :param db_name: Name of the database to connect to
        :return: Database instance
        """
        return self.client[db_name]

    def insert_document(self, db_name, collection_name, document):
        """
        Insert a document into a collection.
        :param db_name: Database name
        :param collection_name: Collection name
        :param document: Document to insert
        :return: Inserted document ID
        """
        db = self.get_database(db_name)
        collection = db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    def fetch_documents(self, db_name, collection_name, query={}):
        """
        Fetch documents from a collection.
        :param db_name: Database name
        :param collection_name: Collection name
        :param query: Query filter (default: fetch all)
        :return: List of documents
        """
        db = self.get_database(db_name)
        collection = db[collection_name]
        return list(collection.find(query))

    def delete_document(self, db_name, collection_name, query):
        """
        Delete a document from a collection.
        :param db_name: Database name
        :param collection_name: Collection name
        :param query: Query filter for deletion
        :return: Deletion result
        """
        db = self.get_database(db_name)
        collection = db[collection_name]
        result = collection.delete_one(query)
        return result.deleted_count
