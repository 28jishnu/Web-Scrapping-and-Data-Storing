import json
from flask import Flask, render_template, request           
from bson import BSON
from bson import json_util
from pymongo import MongoClient
import pandas as pd
import numpy as np
import json
app = Flask(__name__)

@app.route("/register", methods=['POST','GET'])
def register():
  
  if request.method=='POST':

    loc=request.form['location']
    client = MongoClient('mongodb://Jishnu:123jishnu@autotradercluster-shard-00-00-svoxl.mongodb.net:27017,autotradercluster-shard-00-01-svoxl.mongodb.net:27017,autotradercluster-shard-00-02-svoxl.mongodb.net:27017/test?ssl=true&replicaSet=autotraderCluster-shard-0&authSource=admin&retryWrites=true')
    db = client.autotrader
    collection = db['cars']
    cursor = collection.find({})
    var1 = 0
    var2 = 0
    var3 = 0
    db.cars.distinct('location')
    for obj in collection.find():
    #print(obj['location'])
        if loc in obj['location']:
       # print(obj['price'])
            num = obj['price']
            if(num <= 10000):
                var1+=1
            elif(num < 50000 and num >= 10000):
                var2+=1
            else:
                var3+=1
        
   # if(obj['title'].distinct()!= -1):
        #print(obj['title'])
   # count +=1 
 # print(var1)
  #print(count1)
  #print(count2)
    return render_template('location.html', var1=var1, var2=var2, var3=var3)
  else:
    return render_template('locationform.html')
  
  exit()
  
if __name__ == '__main__':
    app.run()