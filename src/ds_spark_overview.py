#coding:utf-8 
import pyspark 
import os 
import matplotlib.pyplot as plt 
myConf      = pyspark.SparkConf() 
spark       = pyspark.sql.SparkSession.builder.master('local').appName('myApp').config(conf=myConf).getOrCreate() 
filepath    = os.path.join('data','ds_spark_overview.txt') 
myRdd         = spark.sparkContext.textFile(filepath) 
wc2         = myRdd.flatMap(lambda x:x.split()).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).map(lambda x:(x[1],x[0])).sortByKey(False).take(30) 
count       = map(lambda x: x[0],wc2) 
word        = map(lambda x: x[1],wc2) 
plt.barh(range(len(count)),count,color='grey') 
plt.yticks(range(len(count)), word) 
plt.show() 