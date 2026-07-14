# Task 08 – Classification Models: Logistic Regression, Decision Trees & Random Forests

## Dataset
scikit-learn's built-in **Breast Cancer Wisconsin (Diagnostic)** dataset
(`sklearn.datasets.load_breast_cancer`) — 569 samples, 30 numeric features
computed from digitized images of breast masses, binary target
(`malignant` = 0, `benign` = 1). Clean, well-known, no missing values, so the
notebook focuses on modeling and evaluation rather than data cleaning.

## Contents
| File | Covers |
|---|---|
| `PKCERT_Task_08_Classification_Models.ipynb` | Main deliverable — all four parts, fully executed with outputs and plots in place |
| `visualizations/` | The 6 charts from the notebook, saved as PNGs |

| Part | What it covers |
|---|---|
| A | Dataset selection/exploration, `train_test_split` + `StandardScaler` + `LogisticRegression`, sigmoid/log-odds working principle, real-world application (medical diagnosis) |
| B | Accuracy/Precision/Recall/F1 (incl. malignant-class recall via `pos_label=0`), confusion matrix + heatmap, per-metric importance explanation |
| C | `DecisionTreeClassifier` (with tree plot), `RandomForestClassifier` (with feature-importance plot), side-by-side confusion matrices, advantages/limitations comparison |
| D | Full metrics comparison table + bar chart across all three models, final recommendation with justification |

## Key Findings (see notebook for full detail)
- **Logistic Regression** achieves the best test-set performance overall:
  98.25% accuracy, 0.9861 F1 (benign), 0.9762 recall on the malignant class —
  the classes are close to linearly separable once features are scaled.
- **Decision Tree** (max_depth=4) trails at 93.86% accuracy — a single tree
  overfits/underfits more than the ensemble or the linear model on this
  dataset.
- **Random Forest** (200 trees) lands in between at 95.61% accuracy, with
  `worst concave points`, `worst radius`, and `worst perimeter` as the
  top-ranked features by importance.
- **Confusion-matrix class convention gotcha**: scikit-learn's binary metrics
  treat class 1 (benign) as "positive" by default, so the clinically
  dangerous error (an actual malignant tumor missed as benign) shows up as a
  **False Positive**, not a False Negative, in `confusion_matrix`'s
  `[[TN,FP],[FN,TP]]` layout — the notebook computes malignant-class recall
  explicitly (`pos_label=0`) rather than relying on the default.
- **Recommendation**: Logistic Regression for deployments where a clinician
  needs interpretable, explainable predictions at comparable accuracy; Random
  Forest if raw predictive robustness across different data splits is the
  only priority.

## Deliverables checklist
- [x] Jupyter notebook with all code, outputs, and plots — `PKCERT_Task_08_Classification_Models.ipynb`
- [x] Logistic Regression model + working principle + real-world application — Part A
- [x] Accuracy/Precision/Recall/F1 + confusion matrix + metric explanations — Part B
- [x] Decision Tree + Random Forest implementation and comparison — Part C
- [x] Comparative analysis + model recommendation — Part D
- [ ] Push to GitHub and add the branch link here

## How to Run
```bash
cd Task_08
jupyter notebook PKCERT_Task_08_Classification_Models.ipynb
# or re-run headlessly end-to-end:
jupyter nbconvert --to notebook --execute --inplace PKCERT_Task_08_Classification_Models.ipynb
```
Requires `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`,
`jupyter`/`jupyterlab` (all already installed). Uses only scikit-learn's
built-in dataset, so no external data files are needed.
