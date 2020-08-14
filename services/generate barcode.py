import pymongo
from pymongo import MongoClient
import barcode
from barcode import generate
from barcode.writer import ImageWriter
# Making a Connection with MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

# Creating a Database
db = client['product_db'] 

#Creating a collection
products = db['products'] 

def create_barcode():
    product_details  = list(products.find())
    product_id = [3423457893475,2987345341209,8472639456194,6453994752945]
    for product,_id in zip(product_details,product_id):
        # product_id = str(dict(product_details[0])["_id"])
        
        product_name = product["name"]
        # print(product_name)
        barcode_type = barcode.get_barcode_class("ean13")
        barcode_number = barcode_type(str(_id))
        barcode_number.save(product_name,options = {"write_text" : False})
        # img = generate('EAN13','1234567890' + product_id,writer = ImageWriter(), output = product_name)
        # print(product_id)
create_barcode()        