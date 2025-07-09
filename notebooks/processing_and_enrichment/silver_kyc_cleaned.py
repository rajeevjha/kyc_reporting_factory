# Clean and validate KYC data
import dlt
from pyspark.sql.functions import *

@dlt.table(name='silver_kyc_cleaned')
def clean_kyc():
    df = dlt.read('bronze_kyc_customers')
    return df.filter(col('customer_id').isNotNull())
