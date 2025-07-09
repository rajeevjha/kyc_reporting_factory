# Enrich KYC data with risk scoring
import dlt
from pyspark.sql.functions import *

@dlt.table(name='gold_kyc_risk_scores')
def risk_score():
    kyc = dlt.read('silver_kyc_cleaned')
    watch = dlt.read('bronze_watchlists')
    return kyc.join(watch, 'name', 'left').withColumn('risk_score', when(col('watchlist_type').isNotNull(), 90).otherwise(10))
