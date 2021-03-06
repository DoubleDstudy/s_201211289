#coding:utf-8 

import os 
import matplotlib.pyplot as plt 
import sys
os.environ["SPARK_HOME"]="C:\users\Admin\Code\s-201211289\spark-2.0.0-bin-hadoop2.7\spark-2.0.0-bin-hadoop2.7"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
print os.environ["PYLIB"]
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))

import pyspark

myConf      = pyspark.SparkConf() 
spark       = pyspark.sql.SparkSession.builder.master('local').appName('myApp').config(conf=myConf).getOrCreate() 
filepath    = os.path.join('data','ds_spark_wiki.txt') 
myRdd         = spark.sparkContext.textFile(filepath) 
wc2         = myRdd.flatMap(lambda x:x.split()).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).map(lambda x:(x[1],x[0])).sortByKey(False).take(30) 
count       = map(lambda x: x[0],wc2) 
word        = map(lambda x: x[1],wc2) 
plt.barh(range(len(count)),count,color='grey') 
plt.yticks(range(len(count)), word) 
plt.show() 