-- SQL dashboard to track KYC risk and quality
SELECT risk_score, COUNT(*) AS customer_count
FROM kyc.gold_kyc_certified_report
GROUP BY risk_score
ORDER BY risk_score DESC;
