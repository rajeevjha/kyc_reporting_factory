# Ingest watchlist data (sanctions, PEP)
import dlt

@dlt.table(name='bronze_watchlists')
def ingest_watchlists():
    return spark.read.option('header', True).csv('abfss://kyc-data@yourstorageacct.dfs.core.windows.net/raw/watchlists.csv')
