# Standard library modules
import os

# Database modules
import pymongo



class database:

    @staticmethod
    def __get_collection():
        client = pymongo.MongoClient(os.environ['MONGO_URI'])
        db = client[os.environ['DB_NAME']]
        collection = db[os.environ['COLLECTION_NAME']]
        return collection
    
    @staticmethod
    def insert_one(name : str, email : str, message : str):
        col = database.__get_collection()
        doc =  {
            'name' : name,
            'email' : email,
            'message' : message
        }
        col.insert_one(doc)
