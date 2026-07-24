# Task 16 – End-to-End Machine Learning Pipeline Project

**Name:** Ahmad Haroon · **Batch:** Batch 2 · **Domain:** AI & Software Development
**Notebook:** `PKCERT_Task_16_End_to_End_ML_Pipeline_Project.ipynb`

## 1. Objective

Build a complete, end-to-end machine learning solution — dataset selection through preprocessing,
model development, evaluation, and documentation — applying the concepts covered across the
internship (Tasks 3–15).

## 2. Dataset

**[Telco Customer Churn](https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv)**
(IBM sample dataset) — 7,043 customers of a telecom company, 21 raw columns.

- **Target:** `Churn` (`Yes`/`No`) — binary classification, whether the customer left last month.
- **Features:** demographics (`gender`, `SeniorCitizen`, `Partner`, `Dependents`), account info
  (`tenure`, `Contract`, `PaperlessBilling`, `PaymentMethod`, `MonthlyCharges`, `TotalCharges`),
  and subscribed services (`PhoneService`, `MultipleLines`, `InternetService`,
  `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`,
  `StreamingMovies`).
- `customerID` is dropped (unique identifier, no predictive value).
- Class balance: **73.5% No Churn / 26.5% Churn** — moderately imbalanced.

## 3. Methodology

### Data cleaning
- `TotalCharges` (loaded as `object`) had 11 blank strings, all `tenure == 0` (brand-new
  customers) — coerced to numeric and imputed to `0`.
- Checked for duplicate rows; kept them, since `customerID` was the only unique key and matches
  on the remaining 20 categorical/numeric columns are plausible coincidences, not guaranteed
  double-counted records.

### Feature engineering
- Collapsed `"No internet service"` / `"No phone service"` into a plain `"No"` across the seven
  service columns (redundant with `InternetService`/`PhoneService`).
- Added `AvgMonthlySpend = TotalCharges / tenure` (smooths billing-cycle noise vs. raw total).
- Added `TenureGroup` (New 0–12mo / Established 1–3yr / Loyal 3yr+) — churn risk is known to be
  concentrated in a customer's first year.

### EDA highlights
- Month-to-month, fiber-optic, electronic-check, short-tenure customers churn at a
  disproportionately high rate — a classic "low switching cost" profile.
- `TotalCharges` correlates strongly with `tenure` (it's a running total), motivating the
  `AvgMonthlySpend` feature over using both raw.

### Pipeline & modeling
- `ColumnTransformer` + `Pipeline`: numeric features → median impute + standard scale;
  categorical features → most-frequent impute + one-hot encode. This guarantees the exact same
  fitted transform is used at train and inference time (no manual leakage risk).
- Three candidates compared with 5-fold stratified cross-validation (ROC-AUC, F1, accuracy):
  **Logistic Regression** (`class_weight="balanced"`), **Random Forest**, **Gradient Boosting**.
- Best model (Logistic Regression, CV ROC-AUC 0.847) tuned further with `GridSearchCV` over
  `C` and `penalty` → best params `C=10, penalty=l2`, CV ROC-AUC 0.8473.

## 4. Results (held-out test set, 1,409 customers)

| Metric | Value |
|---|---|
| ROC-AUC | **0.841** |
| F1 (Churn class) | 0.613 |
| Accuracy | 0.74 |
| Precision / Recall (Churn) | 0.50 / 0.79 |

See `visualizations/6_confusion_matrix_roc.png` for the confusion matrix and ROC curve, and
`visualizations/7_feature_importance.png` for the top drivers (dominated by `Contract`,
`tenure`, and `InternetService`).

## 5. Interpretation, Strengths & Limitations

**Interpretation:** Contract type, tenure, and internet-service type dominate the model's
decisions, consistent with the EDA — short-tenure, month-to-month, fiber customers are highest
risk.

**Strengths**
- ROC-AUC well above random (0.5) and above the majority-class accuracy baseline (~73.5%).
- `class_weight="balanced"` handles the ~3:1 imbalance without synthetic oversampling.
- Single serialized `Pipeline` artifact — no separate scaler/encoder to keep in sync at inference.

**Limitations**
- Single point-in-time snapshot; no usage-trend-over-time features, which would likely help.
- Imbalance still caps recall vs. precision trade-off on the minority (churn) class; the decision
  threshold could be tuned for business cost preferences (missed churner vs. false alarm).
- No external validation set — CV and a held-out split reduce, but don't eliminate, the risk of
  overfitting to this dataset's specific quirks.
- Feature importances reflect the training population; a shift in the customer base (e.g. new
  pricing plans) would require retraining.

## 6. Project Structure

```
Task_16/
├── PKCERT_Task_16_End_to_End_ML_Pipeline_Project.ipynb   # full pipeline, executed end-to-end
├── data/
│   └── Telco-Customer-Churn.csv
├── models/
│   └── telco_churn_pipeline.joblib                       # fitted preprocessing + model
├── visualizations/
│   ├── 1_class_balance.png
│   ├── 2_numeric_distributions_by_churn.png
│   ├── 3_correlation_heatmap.png
│   ├── 4_churn_rate_by_category.png
│   ├── 5_model_comparison_cv.png
│   ├── 6_confusion_matrix_roc.png
│   └── 7_feature_importance.png
└── README.md
```

## 7. Reproducing

```bash
cd Task_16
jupyter nbconvert --to notebook --execute --inplace \
  PKCERT_Task_16_End_to_End_ML_Pipeline_Project.ipynb
```

To use the saved model for inference:

```python
import joblib
pipeline = joblib.load("models/telco_churn_pipeline.joblib")
pipeline.predict(new_customers_df)   # new_customers_df has the same raw columns as the training data
```

## 8. Conclusion

The final Logistic Regression pipeline generalizes well (test ROC-AUC 0.841, close to its CV
score of 0.847, indicating no overfitting), and surfaces actionable churn drivers (contract type,
tenure, internet service) that map directly to retention interventions — e.g., incentivizing
longer contracts or targeting new fiber customers with onboarding support.
