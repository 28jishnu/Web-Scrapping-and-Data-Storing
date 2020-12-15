import json
from flask import Flask, render_template, request           
from bson import BSON
from bson import json_util
from pymongo import MongoClient
import pandas as pd
import numpy as np
import json
app = Flask(__name__)

@app.route("/")
def register():
  

  loc=request.form['location']
  client = MongoClient('mongodb://Jishnu:123jishnu@autotradercluster-shard-00-00-svoxl.mongodb.net:27017,autotradercluster-shard-00-01-svoxl.mongodb.net:27017,autotradercluster-shard-00-02-svoxl.mongodb.net:27017/test?ssl=true&replicaSet=autotraderCluster-shard-0&authSource=admin&retryWrites=true')
  db = client.autotrader
  collection = db['cars']
  cursor = collection.find({})
  var1 = 0
  var2 = 0
  var3 = 0
  agr =  [{'$group': {'_id':"$location" , 'Count': { '$sum': 1 } } } ]
  val = db.cars.aggregate(agr)
  print(list(val))
        
   # if(obj['title'].distinct()!= -1):
        #print(obj['title'])
   # count +=1 
 # print(var1)
  #print(count1)
  #print(count2)
  return render_template('carcount.html', val=val)
  
  exit()
  
if __name__ == '__main__':
    app.run()
