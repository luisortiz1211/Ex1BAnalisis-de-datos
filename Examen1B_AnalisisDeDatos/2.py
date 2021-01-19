import pandas as pd
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))   

response = requests.get("https://www.dakar.com/es/corredores")
soup = BeautifulSoup(response.content, "lxml")

Clasification = []
Motorcycle_riders = []
Country = []

post_pilots=soup.find_all("span", class_="is-ellipsis--xs heading__item heading__name")
post_country=soup.find_all("span", class_="flag flag--text is-uppercase")
post_position=soup.find_all("span", class_="leadFocus__bib")

i=1

for element in post_pilots:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Motorcycle_riders.append(limpio.strip())
    riders={}
    id=i
    try:
        riders['pilots']=Motorcycle_riders
        db.Motorcycle_riders.insert_one(riders)  
        print("Saved sucessful")
        i=i+1
    except Exception as e:    
        print("Saved fail:" + str(e))

#print(Motorcycle_riders)

for element in post_country:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Country.append(limpio.strip())
    country={}
    id=i
    try:
        country['country']= Country
        db.Country.insert_one(country)  
        print("Saved sucessful")
        i=i+1
    except Exception as e:    
        print("Saved fail:" + str(e))

#print(Country)

for element in post_position:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Clasification.append(limpio.strip())
    clasification={}
    id=i
    try:
        clasification['position']=Clasification
        db.Clasification.insert_one()  
        print("Saved sucessful")
        i=i+1
    except Exception as e:    
        print("Saved fail:" + str(e))

#print(Clasification)

#dfDS=pd.DataFrame({'Posicion':Clasification, 'Piloto':Motorcycle_riders,'País':Country})
#print(dfDS)

