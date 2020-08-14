import pymongo
from pymongo import MongoClient

# Making a Connection with MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

# Creating a Database
db = client['product_db'] 

#Creating a collection
products = db['products'] 

new_posts = [ { "_id" : 3423457893471,
                "name": "Apple iPhone XR",
                "rating": 4.5,
                "RAM": 4,
                "ROM": 64,
                "Color" : ["red","white","black","yellow"],
                "price" : 52000},
            { "_id" : 2987345341204,
                "name": "Samsung Galaxy M30s",
                "rating": 4.3,
                "RAM": 4,
                "ROM": 64,
                "Color" : ["black","blue"],
                "price" : 15000},
            {
                "_id" : 8472639456190,
                "name": "OPPO F11",
                "rating": 4.0,
                "RAM": 6,
                "ROM": 128,
                "Color" : ["white","purple","green"],
                "price" : 17000                  
            },
            {
                "_id" : 6453994752945,
                "name": "Panasonic Eluga I8",
                "rating": 4.1,
                "RAM": 4,
                "ROM":64,
                "Color" : ["black"],
                "price" : 12000                  
            },   
            ]
try:            
    insert_product = products.insert_many(new_posts)
    print(f"Inserted id list : {insert_product.inserted_ids}")
except Exception as error:
    print(error)
