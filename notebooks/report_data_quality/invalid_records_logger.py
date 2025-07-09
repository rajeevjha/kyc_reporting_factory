# Log invalid records
import dlt
from pyspark.sql.functions import *

@dlt.table(name='invalid_kyc_records')
@dlt.expect_all_or_drop({
    'valid_customer_id': 'customer_id IS NOT NULL',
    'valid_email': "email LIKE '%@%'"
})
def invalids():
    return dlt.read('bronze_kyc_customers')
