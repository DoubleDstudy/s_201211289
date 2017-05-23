#coding:utf-8 

import os
import sys 
os.environ["SPARK_HOME"]="C:\users\Admin\Code\s-201211289\spark-2.0.0-bin-hadoop2.7\spark-2.0.0-bin-hadoop2.7"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')

sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))

import pyspark
from pyspark.mllib.feature import HashingTF

myConf      = pyspark.SparkConf() 
spark       = pyspark.sql.SparkSession.builder.master('local').appName('myApp').config(conf=myConf).getOrCreate() 
filepath    = os.path.join('data','ds_spark_wiki.txt') 
myRdd         = spark.sparkContext.textFile(filepath) 
documents = myRdd.map(lambda line: line.split(" "))

hashingTF = HashingTF()
tf = hashingTF.transform(documents)
tf.collect()