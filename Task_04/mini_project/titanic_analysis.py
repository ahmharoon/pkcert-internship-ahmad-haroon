"""
Task 04 - Part C: Data Analysis Mini Project (30 Marks)

Reads the Titanic dataset, cleans missing values, generates summary
statistics, and performs basic exploratory data analysis (EDA) using Pandas.
"""

import os
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "titanic.csv")


def load_data(path=DATA_PATH):
    df = pd.read_csv(path)
    print("=" * 60)
    print("1. Load Dataset")
    print("=" * 60)
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print("\nFirst 5 rows:\n", df.head())
    print("\nColumn dtypes:\n", df.dtypes)
    print()
    return df


def clean_data(df):
    print("=" * 60)
    print("2. Data Cleaning")
    print("=" * 60)

    print("Missing values before cleaning:\n", df.isnull().sum())

    df = df.copy()

    # Age: fill missing with the median (robust to outliers)
    df["Age"] = df["Age"].fillna(df["Age"].median())

    # Embarked: fill missing with the most frequent port
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Cabin: mostly missing (~77%) - not usefully imputable, so drop the column
    df = df.drop(columns=["Cabin"])

    # Drop any remaining rows with missing values (should be none left)
    df = df.dropna()

    print("\nMissing values after cleaning:\n", df.isnull().sum())
    print(f"\nShape after cleaning: {df.shape[0]} rows x {df.shape[1]} columns")
    print()
    return df


def summary_statistics(df):
    print("=" * 60)
    print("3. Summary Statistics")
    print("=" * 60)

    print("Numeric summary (describe):\n", df.describe())
    print("\nSurvival counts:\n", df["Survived"].value_counts())
    print("\nSurvival rate overall: {:.1%}".format(df["Survived"].mean()))
    print()


def exploratory_analysis(df):
    print("=" * 60)
    print("4. Exploratory Data Analysis")
    print("=" * 60)

    print("Survival rate by sex:\n", df.groupby("Sex")["Survived"].mean())
    print("\nSurvival rate by passenger class:\n", df.groupby("Pclass")["Survived"].mean())
    print("\nSurvival rate by embarkation port:\n", df.groupby("Embarked")["Survived"].mean())

    print("\nAverage fare by class:\n", df.groupby("Pclass")["Fare"].mean())
    print("\nAverage age by survival:\n", df.groupby("Survived")["Age"].mean())

    df["AgeGroup"] = pd.cut(
        df["Age"], bins=[0, 12, 18, 35, 60, 100],
        labels=["Child", "Teen", "Young Adult", "Adult", "Senior"],
    )
    print("\nSurvival rate by age group:\n", df.groupby("AgeGroup", observed=True)["Survived"].mean())

    print(
        "\nKey findings:\n"
        "- Women had a much higher survival rate than men.\n"
        "- 1st class passengers survived at a higher rate than 2nd/3rd class.\n"
        "- Passengers who paid higher fares (correlated with class) tended to "
        "survive more often.\n"
        "- Children had a relatively higher survival rate than adults, "
        "consistent with a 'women and children first' evacuation policy."
    )
    print()


if __name__ == "__main__":
    raw_df = load_data()
    clean_df = clean_data(raw_df)
    summary_statistics(clean_df)
    exploratory_analysis(clean_df)

    clean_df.to_csv(os.path.join(os.path.dirname(__file__), "titanic_cleaned.csv"), index=False)
    print("Saved cleaned dataset to titanic_cleaned.csv")
