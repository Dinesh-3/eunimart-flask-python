
import pymongo
from pymongo import MongoClient
from flask import Flask,jsonify,render_template,request
import time 
# Making a Connection with MongoClient
client = MongoClient()
client = MongoClient('mongodb://localhost:27017/')

# Creating a Database
db = client['product_db'] 

#Creating a collection
products = db['products'] 

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("barcodes.html")

@app.route("/details")
def details():
    try:
        arg1 = request.args["id"]
        if arg1.isdigit():    
            data = products.find_one({"_id" : int(arg1)})
            if data:
                return jsonify(data)
            else:
                return render_template("404.html")  
        else:
            return "<h1>ID must be an integer !!!"        
    except:
        data = list(products.find())
        return jsonify(data)
@app.route("/login")
def login():
    return render_template("id.html")          
@app.route("/login",methods = ["POST"])
def login1():
    product_id  = request.form["product_id"] 
    if product_id.isdigit():    
            data = products.find_one({"_id" : int(product_id)})
            if data:
                return jsonify(data)
            else:
                return render_template("404.html")  
    else:
        return render_template("interror.html")   
if __name__ == "__main__":
    app.run(debug=True) 







