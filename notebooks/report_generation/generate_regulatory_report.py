# Generate final report as Delta/CSV
from pyspark.sql.functions import *
df = spark.table('kyc_db.gold_kyc_certified_report')
df.write.mode('overwrite').option('header', True).csv('abfss://kyc-data@yourstorageacct.dfs.core.windows.net/export/2025Q3/')
