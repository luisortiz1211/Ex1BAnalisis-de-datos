
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#-------------------------------------------#

ckey='XLiUXmOkCK0WsaLmy2DhhTNp0'
csecret ='GM0AE2n1q60Agr0TbV9nkOD0tlxYOc38ue6NUY3lndJ57uvH8m'
atoken = '1339680483458904068-yccYWCSDHQ2zTuwceyVKg7sEZsHlyU'
asecret = 'YgZBeWZqZq2RdejR4T3YJZYbRm0FPRR1BGNSnQCg88ifq'

#-------------------------------------------#
class listener(StreamListener):
    
    def on_data(self, data):
        dataTweet = json.loads(data)
        try:
            
            dataTweet["_id"] = str(dataTweet['id'])
            doc = db.save(dataTweet)
            print ("Saved sucessful" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
#-------------------------------------------# 

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

#-------------------------------------------#

server = couchdb.Server('http://admin:admin@localhost:5984/') 
try:
    db = server.create('twitter_couch_dakar2021')
except:
    db = server['twitter_couch_dakar2021']
    
#-------------------------------------------#

twitterStream.filter(track=['dakar2021'])
