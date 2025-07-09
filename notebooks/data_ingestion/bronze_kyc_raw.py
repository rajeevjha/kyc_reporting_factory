# Ingest raw KYC CSV files into bronze table
import dlt
from pyspark.sql.functions import *

@dlt.table(name='bronze_kyc_customers')
def ingest_kyc():
    return spark.read.option('header', True).csv('abfss://kyc-data@yourstorageacct.dfs.core.windows.net/raw/customers.csv')
