import pyspark
import numpy
from pyspark.sql import SparkSession
from pyspark.sql import *

class DatasetCleaning:
    def __init__(self, path) -> None:
        self.path = path
        self.spark = SparkSession.builder.appName('DatasetCleaning') \
                                .getOrCreate()
        self.df = self.spark.read.csv(path, header=True, inferSchema=True)
    
    def select(self, *column_names) -> pyspark.sql.DataFrame:
        return self.df.select(*column_names)
    
    def remove_null(self) -> pyspark.sql.DataFrame:
        self.df
        
    

file_path = "Python3/python_project/Pyspark_projects/OnlineSalesDataset-CartData-CLEAN.csv"
spark = SparkSession.builder.appName('train').getOrCreate()
# data = DatasetCleaning(file_path)
# data = data.select('SKU','Barcode','Quantity','Price','Type','Category')
# print(data.show())
    