# Task 05 – Data Preprocessing, Visualization & SQL Fundamentals

## Dataset
`apple_products_pricing_2020_2026.csv` — 80,000 rows, 14 columns of Apple
product listings scraped from Amazon and Flipkart between 2020 and 2026.

| Column | Description |
|---|---|
| Date | Listing date |
| Platform | Amazon or Flipkart |
| Product_Category | Watch, iPad, iPhone, Mac |
| Model_Name | Specific model/configuration (31 unique) |
| Condition | New or Renewed/Refurbished |
| Launch_Price_USD / Launch_Price_INR | Original launch price |
| Current_Price_USD / Current_Price_INR | Current listed price |
| Discount_Pct | % discount vs. launch price |
| Sale_Event | Promotional event, if any (Black Friday, Prime Day, etc.) |
| Stock_Status | In Stock / Low Stock / Out of Stock |
| Rating | Average customer rating |
| Reviews_Count | Number of reviews |

## Contents
| File | Covers |
|---|---|
| `part_a_data_cleaning.py` | Part A (30): missing values, duplicates, outliers (IQR) -> `apple_products_pricing_cleaned.csv` |
| `part_b_visualization.py` | Part B (25): histogram, boxplot, correlation heatmap, +2 charts -> `visualizations/` |
| `part_c_feature_engineering.py` | Part C (20): categorical identification, one-hot + label encoding, standardization -> `apple_products_pricing_engineered.csv` |
| `part_d_sql_fundamentals.py` | Part D (25): builds `apple_products_pricing.db` (SQLite), SELECT/WHERE/GROUP BY/JOIN queries |
| `PKCERT_Task_05_Deliverables.docx` | Full write-up: source code, outputs, and insights for all four parts |

## Data Cleaning Summary (Part A)
- **Missing values**: only `Sale_Event` had gaps (73,351 of 80,000 rows), all
  representing "not part of a sale" rather than a data error — filled with
  the explicit label `"No Sale"` instead of being dropped or statistically
  imputed.
- **Duplicates**: none found.
- **Outliers**: detected via the IQR method. `Current_Price_USD` (5,076) and
  `Reviews_Count` (2,628) had values beyond the IQR bounds; these reflect
  genuine premium-product prices and highly-reviewed popular models rather
  than data-entry errors, so they were winsorized (capped at the IQR
  bounds) rather than dropped, to avoid losing rows.
- `Date` was converted from string to a proper `datetime` column.

## Feature Engineering Summary (Part C)
- **One-Hot Encoded** (low cardinality, nominal): `Platform`, `Condition`,
  `Stock_Status`, `Sale_Event`.
- **Label Encoded** (higher cardinality): `Product_Category`, `Model_Name`.
- **Standardized** (`StandardScaler`, zero mean / unit variance):
  `Launch_Price_USD`, `Current_Price_USD`, `Discount_Pct`, `Rating`,
  `Reviews_Count` — needed because these columns live on very different
  raw scales (e.g. price in hundreds/thousands vs. rating 3.8-4.9), which
  would otherwise dominate distance- or gradient-based algorithms.

## Database Schema (Part D)
Two related SQLite tables built from the cleaned data:
- **`products`** (31 rows) — one row per distinct model: `product_id` (PK),
  `Model_Name`, `Product_Category`, `Launch_Price_USD`.
- **`sales`** (80,000 rows) — one row per listing observation:
  `sale_id` (PK), `product_id` (FK -> products), `Date`, `Platform`,
  `Condition`, `Current_Price_USD`, `Discount_Pct`, `Sale_Event`,
  `Stock_Status`, `Rating`, `Reviews_Count`.

This normalized split is what makes the JOIN query meaningful (aggregating
`sales` back up to the `products` dimension).

## How to Run
```bash
cd Task_05
python3 part_a_data_cleaning.py        # -> apple_products_pricing_cleaned.csv
python3 part_b_visualization.py        # -> visualizations/*.png
python3 part_c_feature_engineering.py  # -> apple_products_pricing_engineered.csv
python3 part_d_sql_fundamentals.py     # -> apple_products_pricing.db + query output
```
Requires `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn` (all
already installed via Anaconda) and the built-in `sqlite3` module.

Run Part A before Parts B/C/D — they read the cleaned CSV it produces.
