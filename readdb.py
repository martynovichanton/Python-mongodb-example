from pymongo import MongoClient

client = MongoClient("mongodb://anton:XXXXX@localhost:27017/")
db=client.business
result=db.reviews.find()
for doc in result:
    print(doc)