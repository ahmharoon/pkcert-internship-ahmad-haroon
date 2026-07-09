"""
Task 05 - Part A: Data Cleaning & Preprocessing (30 Marks)
1. Load the dataset
2. Handle missing values, duplicate records, and outliers
3. Report explaining each preprocessing step
"""

import os
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "apple_products_pricing_2020_2026.csv")
CLEANED_PATH = os.path.join(os.path.dirname(__file__), "apple_products_pricing_cleaned.csv")

NUMERIC_COLS = ["Launch_Price_USD", "Current_Price_USD", "Discount_Pct", "Rating", "Reviews_Count"]


def load_data(path=DATA_PATH):
    print("=" * 70)
    print("1. Load Dataset")
    print("=" * 70)
    df = pd.read_csv(path)
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print("\nColumns and dtypes:\n", df.dtypes)
    print("\nFirst 5 rows:\n", df.head())
    print()
    return df


def handle_missing_values(df):
    print("=" * 70)
    print("2. Missing Values")
    print("=" * 70)

    df = df.copy()
    missing_before = df.isnull().sum()
    print("Missing values per column (before):\n", missing_before[missing_before > 0])

    # Sale_Event is NaN whenever a record was not part of a promotional sale
    # event. That is meaningful information, not a data-entry gap, so it is
    # filled with the explicit label "No Sale" rather than dropped/imputed
    # statistically.
    df["Sale_Event"] = df["Sale_Event"].fillna("No Sale")

    missing_after = df.isnull().sum()
    print("\nMissing values per column (after):\n", missing_after[missing_after > 0] if missing_after.sum() else "None remaining")
    print()
    return df


def handle_duplicates(df):
    print("=" * 70)
    print("3. Duplicate Records")
    print("=" * 70)

    df = df.copy()
    dup_count = df.duplicated().sum()
    print(f"Exact duplicate rows found: {dup_count}")
    if dup_count:
        df = df.drop_duplicates()
        print(f"Dropped {dup_count} duplicate rows. New shape: {df.shape}")
    else:
        print("No duplicate rows to remove.")
    print()
    return df


def handle_outliers(df):
    print("=" * 70)
    print("4. Outliers (IQR method)")
    print("=" * 70)

    df = df.copy()
    for col in NUMERIC_COLS:
        q1, q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        outlier_count = ((df[col] < lower) | (df[col] > upper)).sum()
        print(f"{col:20s} bounds=({lower:8.2f}, {upper:8.2f})  outliers={outlier_count}")

        if outlier_count:
            # Winsorize (clip) rather than drop: high-end MacBook/iPhone Pro
            # prices and highly-reviewed popular models are genuine values,
            # not data errors, so capping preserves the rows while limiting
            # the influence of extreme values on later stats/models.
            df[col] = df[col].clip(lower=lower, upper=upper)

    print("\nOutliers were capped (winsorized) at the IQR bounds instead of")
    print("dropped, since they reflect real premium-product pricing/review")
    print("patterns rather than data-entry errors.")
    print()
    return df


def convert_dtypes(df):
    print("=" * 70)
    print("5. Data Type Conversion")
    print("=" * 70)
    df = df.copy()
    df["Date"] = pd.to_datetime(df["Date"])
    print("Converted 'Date' column to datetime.")
    print(f"Date range: {df['Date'].min().date()} to {df['Date'].max().date()}")
    print()
    return df


def main():
    df = load_data()
    df = handle_missing_values(df)
    df = handle_duplicates(df)
    df = handle_outliers(df)
    df = convert_dtypes(df)

    print("=" * 70)
    print("6. Final Cleaned Dataset")
    print("=" * 70)
    print(f"Final shape: {df.shape}")
    print(df.describe(include="all").transpose())

    df.to_csv(CLEANED_PATH, index=False)
    print(f"\nCleaned dataset saved to: {CLEANED_PATH}")


if __name__ == "__main__":
    main()
