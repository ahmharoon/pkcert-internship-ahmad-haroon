# Task 07 – Machine Learning Foundations: Train/Test Split, Model Fit, and Linear Regression

## Datasets
- **Parts A & C** — scikit-learn's built-in **diabetes** dataset (442 rows,
  10 numeric features, no missing values). Small and clean, so it keeps the
  theory demos (split shapes, coefficients, MSE/R²) easy to follow.
- **Part B** — a synthetic sine-curve dataset (`y = sin(2πx) + noise`, 60
  points). The standard way to visualize the bias-variance tradeoff, since
  the true function is known and polynomial degree directly controls model
  complexity.
- **Part D & Bonus** — the raw `apple_products_pricing_2020_2026.csv` from
  [`../Task_05`](../Task_05), reused here (not duplicated) as a real, messy
  80,000-row dataset with a genuinely missing column (`Sale_Event`) and five
  categorical columns to encode, for the "practical coding session" part of
  the task. Target: `Current_Price_USD`.

## Contents
| File | Covers |
|---|---|
| `PKCERT_Task_07_ML_Foundations.ipynb` | Main deliverable — all four parts + bonus, fully executed with outputs and plots in place |
| `visualizations/` | The 3 charts from the notebook, saved as PNGs |
| `screenshots/` | The 2 required screenshots — Python environment check and Linear Regression evaluation metrics |

| Part | What it covers |
|---|---|
| A | Why/how to train-test split, typical ratios, `train_test_split` demo, `random_state`, validation vs. test set |
| B | Overfitting/underfitting definitions, bias-variance tradeoff, 5 mitigation techniques, train-vs-test-error-by-complexity plot |
| C | Linear regression math (simple + multiple), normal equation vs. gradient descent, full fit + MSE/R² + predicted-vs-actual plot on the diabetes dataset |
| D | Raw CSV cleaning + one-hot encoding, `load_data()`/`split_data()`/`train_model()`/`evaluate_model()` reusable functions, 60/40 vs 80/20 vs 90/10 split comparison table, 5-fold cross-validation, learning curve |
| Bonus | Degree-2/3 polynomial regression vs. plain linear regression, compared with the same Part D functions |

## Key Findings (see notebook for full detail)
- **Bias-variance demo (Part B)**: fitting polynomials of degree 1–15 to the
  synthetic sine data shows the classic U-shape — degree 1 underfits (high
  error on both train and test), degree 15 overfits (near-zero training
  error but test error climbing back up), and degree 5 minimizes test error.
- **Diabetes linear regression (Part C)**: R² ≈ 0.45 on held-out data — a
  real but partial linear relationship, expected from only 10 features on a
  small medical dataset.
- **Apple pricing split-ratio comparison (Part D)**: train and test R²
  (~0.981) stay essentially flat across 60/40, 80/20, and 90/10 splits —
  with 80,000 rows, the exact split ratio barely matters.
- **Learning curve (Part D)**: training and cross-validation R² converge to
  ~0.98 and plateau — more data isn't the bottleneck; the *linear* model's
  bias is.
- **Polynomial bonus**: the standout result. Degree-2 polynomial features
  push R² from 0.979 to essentially 1.0000 on **both** train and test
  (RMSE $68 → $0.31), because `Current_Price_USD` is generated as
  `Launch_Price_USD * (1 − Discount_Pct/100)` — a genuine multiplicative
  interaction that a plain linear model structurally cannot represent but a
  degree-2 interaction term captures almost exactly. Since test improves in
  lockstep with train, this is polynomial features fixing **underfitting**,
  not causing overfitting.

## Deliverables checklist
- [x] Jupyter notebook with all code, outputs, and plots — `PKCERT_Task_07_ML_Foundations.ipynb`
- [x] Written explanation of train/test split, overfitting/underfitting, bias-variance tradeoff — markdown cells in Parts A & B of the notebook
- [x] Screenshot of the Python environment (sklearn/pandas/numpy/matplotlib) — `screenshots/1_python_environment.png`
- [x] Screenshot of the trained Linear Regression model's evaluation metrics — `screenshots/2_linear_regression_evaluation_metrics.png`
- [x] GitHub repository link with notebook and README pushed — https://github.com/ahmharoon/pkcert-internship-ahmad-haroon/tree/Task-07/Task_07

## How to Run
```bash
cd Task_07
jupyter notebook PKCERT_Task_07_ML_Foundations.ipynb
# or re-run headlessly end-to-end:
jupyter nbconvert --to notebook --execute --inplace PKCERT_Task_07_ML_Foundations.ipynb
```
Requires `pandas`, `numpy`, `matplotlib`, `scikit-learn`, `jupyter`/`jupyterlab`
(all already installed via Anaconda). Parts D and Bonus read
`../Task_05/apple_products_pricing_2020_2026.csv`, so `Task_05/` must be
present alongside `Task_07/`.
