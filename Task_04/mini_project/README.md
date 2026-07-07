# Titanic Survival – Data Analysis Mini Project

## Dataset
The [Titanic dataset](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)
(`titanic.csv`, 891 rows, 12 columns) contains passenger-level records from
the RMS Titanic, including demographic info (age, sex), ticket class,
fare paid, port of embarkation, and whether the passenger survived.

| Column | Description |
|---|---|
| PassengerId | Unique passenger identifier |
| Survived | 0 = did not survive, 1 = survived (target variable) |
| Pclass | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd) |
| Name, Sex, Age | Passenger demographics |
| SibSp | # of siblings/spouses aboard |
| Parch | # of parents/children aboard |
| Ticket, Fare | Ticket number and fare paid |
| Cabin | Cabin number (mostly missing) |
| Embarked | Port of embarkation (C, Q, S) |

## Data Cleaning Process
1. **Age** (177 missing values) — filled with the column median, since age is
   numeric and roughly right-skewed; the median is robust to outliers.
2. **Embarked** (2 missing values) — filled with the mode (most frequent
   port), a reasonable default for a categorical column with very few gaps.
3. **Cabin** (687 missing values, ~77% of the column) — dropped entirely
   rather than imputed, since that much missingness makes any fill
   unreliable and not usefully informative.
4. Any remaining rows with nulls were dropped as a final safety net (none
   remained after the steps above).

The cleaned dataset is saved to `titanic_cleaned.csv`.

## Analysis Performed
- Overall summary statistics (`describe()`) for numeric columns.
- Overall survival rate.
- Survival rate broken down by: sex, passenger class, embarkation port, and
  age group (Child/Teen/Young Adult/Adult/Senior via `pd.cut`).
- Average fare by class and average age by survival outcome.

## Key Findings
- **Sex was the strongest predictor of survival**: ~74% of women survived
  vs. ~19% of men.
- **Passenger class mattered**: 1st class survival rate (~63%) was more
  than double 3rd class (~24%).
- **Fare correlates with class**: average 1st class fare (~$84) was over
  6x the average 3rd class fare (~$14), reinforcing that wealthier,
  higher-class passengers had better survival odds.
- **Children survived at a higher rate (~58%)** than adults or seniors,
  consistent with the "women and children first" evacuation protocol.
- Passengers who embarked at Cherbourg (C) had a notably higher survival
  rate (~55%) than those from Southampton (S) (~34%), likely reflecting
  that Cherbourg had a higher proportion of 1st class passengers.

## How to Run
```bash
cd mini_project
python3 titanic_analysis.py
```
Requires `pandas` (already installed via Anaconda). The script reads
`titanic.csv`, prints the full analysis to the console, and writes
`titanic_cleaned.csv`.
