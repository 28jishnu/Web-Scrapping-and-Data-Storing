import json
from flask import Flask, render_template, request           
from bson import BSON
from bson import json_util
from pymongo import MongoClient
import pandas as pd
import numpy as np
import json
    
            
        
app = Flask(__name__)
    
@app.route("/", methods=['POST','GET'])
def index():
      
    if request.method=='POST':
        return render_template('location.html')
    else:
        return render_template('index.html')
      
    exit()
    
@app.route("/register", methods=['POST','GET'])
def register():
      
    if request.method=='POST':
        carinsert = dict()
        price=request.form['price']
        loc=request.form['location']
        title=request.form['title']
        mil=request.form['milage']
        print(price)
        client = MongoClient('mongodb://Jishnu:123jishnu@autotradercluster-shard-00-00-svoxl.mongodb.net:27017,autotradercluster-shard-00-01-svoxl.mongodb.net:27017,autotradercluster-shard-00-02-svoxl.mongodb.net:27017/test?ssl=true&replicaSet=autotraderCluster-shard-0&authSource=admin&retryWrites=true')
        db = client.autotrader
        collection = db['cars']
        cursor = collection.find({})
        carinsert["title"]=title
        carinsert["location"]=loc
        carinsert["price"]=price
        carinsert["milage"]=mil
        idcount =0
        for obj in collection.find():
        
            if(idcount<=obj['ID']):
                idcount=obj['ID']
        idcount=idcount+1
        carinsert["ID"]=idcount
        print(carinsert)
        collection.insert(carinsert) 
        
        
        #db.cars.distinct('location')
        #for obj in collection.find():
        #print(obj['location'])
         #   if loc in obj['location']:
           # print(obj['price'])
          #      num = obj['price']
           #     if(num <= 10000):
            #        var1+=1
             #   elif(num < 50000 and num >= 10000):
              #      var2+=1
               # else:
                #    var3+=1
                
       # if(obj['title'].distinct()!= -1):
            #print(obj['title'])
       # count +=1 
     # print(var1)
      #print(count1)
      #print(count2)
        return render_template('success.html')
    else: 
        return render_template('locationform.html')
      
    exit()
     
@app.route("/delete", methods=['POST','GET'])
def delete():
    if request.method=='POST':
        myquery= dict()  
        client = MongoClient('mongodb://Jishnu:123jishnu@autotradercluster-shard-00-00-svoxl.mongodb.net:27017,autotradercluster-shard-00-01-svoxl.mongodb.net:27017,autotradercluster-shard-00-02-svoxl.mongodb.net:27017/test?ssl=true&replicaSet=autotraderCluster-shard-0&authSource=admin&retryWrites=true')
        db = client.autotrader
        collection = db['cars']
        cursor = collection.find({})
        dele=int(request.form['id1'])
    
        print(dele)
        myquery['ID']=dele
        print(myquery)
        collection.delete_one(myquery)
        return render_template('success1.html')
    else:
        return render_template('deleteform.html')
    exit()
    
@app.route("/readsel", methods=['POST','GET'])
def readsel():
    return render_template('readsel.html')
        
    exit()
        
@app.route("/readid", methods=['POST','GET'])
def readid():
    if request.method=='POST':
        myquery= dict()  
        client = MongoClient('mongodb://Jishnu:123jishnu@autotradercluster-shard-00-00-svoxl.mongodb.net:27017,autotradercluster-shard-00-01-svoxl.mongodb.net:27017,autotradercluster-shard-00-02-svoxl.mongodb.net:27017/test?ssl=true&replicaSet=autotraderCluster-shard-0&authSource=admin&retryWrites=true')
        db = client.autotrader
        collection = db['cars']
        id1=int(request.form['id1'])
        for obj in collection.find():
    #print(obj['location'])
            if id1 == obj['ID']:
                price=obj['price']
                loc=obj['location']
                milage=obj['milage']
                title=obj['title']
        return render_template('tableid.html',id1=id1,title=title,price=price,loc=loc,milage=milage)
    else:
        return render_template('readidform.html')
    exit()
        
@app.route("/readloc", methods=['POST','GET'])
def readloc():
    if request.method=='POST':
        client = MongoClient('mongodb://Jishnu:123jishnu@autotradercluster-shard-00-00-svoxl.mongodb.net:27017,autotradercluster-shard-00-01-svoxl.mongodb.net:27017,autotradercluster-shard-00-02-svoxl.mongodb.net:27017/test?ssl=true&replicaSet=autotraderCluster-shard-0&authSource=admin&retryWrites=true')
        db = client.autotrader
        collection = db['cars']
        cursor = collection.find({})
        loc=request.form['loc']
        tabledatas=[]
        
        for document in cursor:
            myquery=dict()
            if loc in  document['location']:
                myquery['ID']=document['ID']
                myquery['title']=document['title']
                myquery['location']=document['location']
                myquery['price']=document['price']
                myquery['milage']=document['milage']
                tabledatas.append(myquery)
                
    
        return render_template('tableid1.html',tabledatas=tabledatas)
    else:
        return render_template('readlocform.html')
    exit()
        
@app.route("/readtitle", methods=['POST','GET'])
def readtitle():
    if request.method=='POST':
        client = MongoClient('mongodb://Jishnu:123jishnu@autotradercluster-shard-00-00-svoxl.mongodb.net:27017,autotradercluster-shard-00-01-svoxl.mongodb.net:27017,autotradercluster-shard-00-02-svoxl.mongodb.net:27017/test?ssl=true&replicaSet=autotraderCluster-shard-0&authSource=admin&retryWrites=true')
        db = client.autotrader
        collection = db['cars']
        cursor = collection.find({})
        ttl=request.form['ttl']
        tabledatas=[]
        print(ttl)
        for document in cursor:
            myquery=dict()
            title=document['title']
            if ttl in title:
                myquery['ID']=document['ID']
                myquery['title']=document['title']
                myquery['location']=document['location']
                myquery['price']=document['price']
                myquery['milage']=document['milage']
                tabledatas.append(myquery)
                
    
        return render_template('tabletitle.html',tabledatas=tabledatas)
    else:
        return render_template('readttlform.html')
    exit()
      
if __name__ == '__main__':
    app.run()