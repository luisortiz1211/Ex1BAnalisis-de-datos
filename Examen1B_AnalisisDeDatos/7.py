from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import dns
import json


CLIENT = couchdb.Server('http://admin:admin@localhost:5984/')

try:
    print('cocuh connection: Success')
except ConnectionFailure as e:
    print('Couch connection: failed', e)
    
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

client = pymongo.MongoClient("mongodb+srv://esfot:esfot@cluster0.p8olh.mongodb.net/twitter_couch_dakar2021?retryWrites=true&w=majority")
DBm = client.get_database('twitter_couch_dakar2021')
DBma =DBm.couchdakar2021

try:
    client.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as e:
    print('MongoDB Atlas connection: failed', e)
    
DBc=CLIENT['twitter_couch_dakar2021']

for db in DBc:
    try:
        DBma.insert_one(DBc[db])
        print('Data saved mongoDB Atlas')
    except TypeError as et:
        print('current document raised error: {}'.format(et))
        SKIPPED.append(db)  
        continue   
    except Exception as e:
        raise e