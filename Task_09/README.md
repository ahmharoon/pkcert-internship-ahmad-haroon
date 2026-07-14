# Task 09 – Support Vector Machines (SVM) & k-Nearest Neighbors (kNN)

## Dataset
scikit-learn's built-in **Breast Cancer Wisconsin (Diagnostic)** dataset
(`sklearn.datasets.load_breast_cancer`) — reused from
[`../Task_08`](../Task_08) for continuity. 569 samples, 30 numeric features,
binary target (`malignant` = 0, `benign` = 1), no missing values. A good fit
here because both SVM and kNN are distance/margin-based and therefore
genuinely need the `StandardScaler` preprocessing this task asks for.

## Contents
| File | Covers |
|---|---|
| `PKCERT_Task_09_SVM_kNN.ipynb` | Main deliverable — all four parts, fully executed with outputs and plots in place |
| `visualizations/` | The 4 charts from the notebook, saved as PNGs |

| Part | What it covers |
|---|---|
| A | Dataset description, missing-value/encoding check, `StandardScaler` scaling, `train_test_split` |
| B | SVM: kernel comparison (linear/rbf/poly) with the best kept, full metrics + confusion matrix, explanation of SVM (margin, kernel trick, advantages/limitations/applications) |
| C | kNN: K sweep (1–25, odd) with accuracy-vs-K plot to justify the chosen K, full metrics + confusion matrix, explanation of kNN (advantages/limitations/applications) |
| D | SVM vs. kNN comparison table + bar chart, final recommendation with justification |

## Key Findings (see notebook for full detail)
- **Kernel sweep**: `rbf` wins (98.25% accuracy) over `linear` (97.37%) and
  `poly` (91.23%) — the classes are close to linearly separable but a slight
  curvature in the boundary still helps.
- **K sweep**: `K=3` maximizes test accuracy (98.25%) over the 1–25 odd range.
- **SVM (rbf) vs. kNN (K=3)** tie on overall accuracy (0.9825), but **SVM
  leads clearly on malignant-class recall** (0.976 vs. kNN's 0.952) — the
  metric that matters most for a cancer-screening use case, since it measures
  how many actual malignant cases are *not* missed.
- **Recommendation**: SVM, because it matches kNN's accuracy while catching
  more true malignant cases; kNN remains a reasonable, cheap baseline.

## Deliverables checklist
- [x] Dataset description, preprocessing (missing values/encoding/scaling), train/test split — Part A
- [x] SVM model + kernel justification + metrics + confusion matrix + explanation — Part B
- [x] kNN model + K justification + metrics + confusion matrix + explanation — Part C
- [x] Comparative analysis + recommendation — Part D
- [ ] Push to GitHub and add the branch link here

## How to Run
```bash
cd Task_09
jupyter notebook PKCERT_Task_09_SVM_kNN.ipynb
# or re-run headlessly end-to-end:
jupyter nbconvert --to notebook --execute --inplace PKCERT_Task_09_SVM_kNN.ipynb
```
Requires `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`,
`jupyter`/`jupyterlab` (all already installed). Uses only scikit-learn's
built-in dataset, so no external data files are needed.
