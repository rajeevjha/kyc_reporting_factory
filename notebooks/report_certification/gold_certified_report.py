# Certify gold report with metadata
import dlt
from pyspark.sql.functions import *

@dlt.table(name='gold_kyc_certified_report')
def certify():
    df = dlt.read('gold_kyc_risk_scores')
    return df.withColumn('certified_by', lit('compliance_officer@datacorp.com')).withColumn('certified_at', current_timestamp())
