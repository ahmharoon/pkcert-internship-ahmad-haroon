# Task 06 – Exploratory Data Analysis (EDA) Using Jupyter Notebook

## Dataset
`archive/` — a synthetic "FIFA World Cup 2026 social media sentiment &
engagement" dataset, split across four related CSVs:

| File | Rows | Role |
|---|---|---|
| `social_media_posts.csv` | 100 | Raw social media posts (platform, sentiment, engagement) |
| `match_context.csv` | 20 | Match details (teams, score, venue, weather) |
| `stakeholders.csv` | 20 | Influencer/journalist/sponsor/FIFA profiles |
| `host_city_context.csv` | 5 | City-level stats — **not used**, city naming is inconsistent with the other files (see notebook Part B.2) |
| `merged_master.csv` | 100 | Posts pre-joined with match context (provided) |

The notebook loads `merged_master.csv` and additionally joins in
`stakeholders.csv` on `stakeholder_id`, giving a 100-row × 45-column
analysis table.

## Contents
| File | Covers |
|---|---|
| `PKCERT_Task_06_EDA_Analysis.ipynb` | Main deliverable — Part A (dataset selection), Part B (structure/missing-values/duplicates/inconsistencies + 6 visualizations with interpretation), Part C (written findings, insights, limitations), Part D (notebook organization) |
| `visualizations/` | The 6 charts from the notebook, saved as PNGs |
| `PKCERT_Task_06_Deliverables.docx` | Report version of the notebook (source + outputs + charts + insights) |

## Key Findings (see notebook for full detail)
- No missing values or duplicates in the merged dataset, but several
  data-generation inconsistencies were found and documented: `winner` is
  `"TBD"` for every match despite scores being populated, `stage`/`device`/
  `source` are constant across all rows, and `host_city_context.csv` uses
  real city names that don't match the placeholder city labels
  (`City0`-`City4`) used elsewhere — so it was excluded from the join.
- Sentiment is fairly balanced (37% positive / 36% negative / 27% neutral).
- Engagement rate is roughly uniform across 1%-10%, with a small spike of
  standout posts near the top of the range.
- Only `likes` and `views` are strongly correlated (r ≈ 0.79) among the raw
  engagement counts; `comments` and `shares` move mostly independently.
- Sponsorship/Travel topics out-engage Fan Experience/Match Performance
  content — the opposite of what "emotional content wins" would predict.
- Players and Journalists post more positively on average than Sponsors and
  official FIFA accounts.

## How to Run
```bash
cd Task_06
jupyter notebook PKCERT_Task_06_EDA_Analysis.ipynb
# or re-run headlessly end-to-end:
jupyter nbconvert --to notebook --execute --inplace PKCERT_Task_06_EDA_Analysis.ipynb
```
Requires `pandas`, `numpy`, `matplotlib`, `seaborn`, `jupyter`/`jupyterlab`
(all already installed via Anaconda).
