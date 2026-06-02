
-- 1. TOP 5 FUNDS BY AUM

SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM cleaned_03_aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2. AVERAGE NAV PER MONTH

SELECT substr(date, 1, 7) AS month,
       AVG(nav) AS avg_nav
FROM cleaned_nav_history
GROUP BY month;

-- 3. SIP YOY GROWTH

SELECT month,
       yoy_growth_pct
FROM cleaned_04_monthly_sip_inflows;

-- 4. TRANSACTIONS BY STATE

SELECT state,
       COUNT(*) AS total_transactions
FROM cleaned_investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. FUNDS WITH LOW EXPENSE RATIO

SELECT scheme_name,
       expense_ratio_pct
FROM cleaned_scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. AVERAGE RETURN BY CATEGORY

SELECT category,
       AVG(return_3yr_pct)
FROM cleaned_scheme_performance
GROUP BY category;

-- 7. TOTAL REDEMPTIONS

SELECT SUM(amount_inr)
FROM cleaned_investor_transactions
WHERE transaction_type = 'REDEMPTION';

-- 8. MOST POPULAR CITY

SELECT city,
       COUNT(*) AS investors
FROM cleaned_investor_transactions
GROUP BY city
ORDER BY investors DESC
LIMIT 10;

-- 9. HIGHEST SHARPE RATIO

SELECT scheme_name,
       sharpe_ratio
FROM cleaned_scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 10. TOTAL INDUSTRY FOLIOS

SELECT month,
       total_folios_crore
FROM cleaned_06_industry_folio_count;

