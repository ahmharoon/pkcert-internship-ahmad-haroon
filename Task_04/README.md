# Task 04 – NumPy & Pandas for Data Analysis

## Contents
| File | Covers |
|---|---|
| `part_a_numpy_fundamentals.py` | Part A (40): array creation, indexing/slicing/reshaping, broadcasting, vectorization vs loops, linear algebra |
| `part_b_pandas_fundamentals.py` | Part B (30): Series/DataFrame, indexing/filtering/sorting, groupby, merge/join |
| `mini_project/` | Part C (30): Titanic EDA mini project (dataset, analysis script, README) — see its own README for details |

## How to Run
```bash
cd Task_04
python3 part_a_numpy_fundamentals.py
python3 part_b_pandas_fundamentals.py
cd mini_project && python3 titanic_analysis.py
```
Requires `numpy` and `pandas`, both already installed via Anaconda.

## Uploading the Mini Project to GitHub
Part C requires the mini project to be pushed to a GitHub repository. From
inside `mini_project/`:
```bash
git init
git add .
git commit -m "Titanic EDA mini project - PKCERT Task 04"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```
Create the empty repo on GitHub first (via the website or `gh repo create`),
then run the commands above.
