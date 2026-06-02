
## 01_fund_master.csv

| Column | Type | Description |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | AMC / fund house |
| category | TEXT | Fund category |
| sub_category | TEXT | Detailed category |
| expense_ratio_pct | FLOAT | Expense ratio percentage |

---

## 02_nav_history.csv

| Column | Type | Description |
|---|---|---|
| amfi_code | INTEGER | Scheme code |
| date | DATE | NAV date |
| nav | FLOAT | Net Asset Value |

Continue similarly for remaining datasets.