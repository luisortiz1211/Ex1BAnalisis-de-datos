import pandas as pd
import pymongo 


client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.get_database('couch_mongo_dakar2021')
collection = db.get_collection('dakar2021')
df = pd.DataFrame(list(collection.find()))

try:
	df.to_csv('couch_mongo_dakar2021.csv', index=False)
	print("Saved sucessful ")
except Exception as e:
	raise e
	print("Already exists")
	
