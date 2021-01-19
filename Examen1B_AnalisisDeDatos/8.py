from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import dns
import json

CLIENT = pymongo.MongoClient('mongodb://localhost:27017')

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as e:
    print('MongoDB connection: failed', e)
    
client = pymongo.MongoClient("mongodb+srv://esfot:esfot@cluster0.p8olh.mongodb.net/couch_mongo_dakar2021?retryWrites=true&w=majority")
DBm = client.get_database('couch_mongo_dakar2021')
DBma = DBm.dakar2021


try:
    client.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as e:
    print('MongoDB Atlas connection: failed', e)
    

DBS = ['couch_mongo_dakar2021']

for db in DBS:
    if db not in ('admin', 'local','config'):  
        cols = CLIENT[db].list_collection_names()  
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    documents = json.loads(json_util.dumps(x))
                    ##print(documents)
                    #doc=DBS.count(documents)
                    DBma.insert_one(documents)
                    print("saved in mongo atlas")

                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  # creating list of skipped documents for later analysis
                    continue    # continue to next document
                except Exception as e:
                    raise e