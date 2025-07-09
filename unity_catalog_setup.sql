
CREATE SCHEMA IF NOT EXISTS main.kyc_db
COMMENT 'Schema for KYC Reporting Factory data'
MANAGED LOCATION 'abfss://kyc-data@yourstorageacct.dfs.core.windows.net/managed';

CREATE EXTERNAL LOCATION kyc_ext_loc
  URL 'abfss://kyc-data@yourstorageacct.dfs.core.windows.net/'
  WITH CREDENTIAL service_principal_credential
  COMMENT 'External location for KYC raw & processed data';
