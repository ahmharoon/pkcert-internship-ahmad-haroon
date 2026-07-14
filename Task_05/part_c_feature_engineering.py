"""
Task 05 - Part C: Feature Engineering (20 Marks)
1. Identify categorical features.
2. Apply One-Hot Encoding and/or Label Encoding.
3. Normalize/standardize numeric features and explain the importance.
"""

import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

BASE_DIR = os.path.dirname(__file__)
CLEANED_PATH = os.path.join(BASE_DIR, "apple_products_pricing_cleaned.csv")
ENGINEERED_PATH = os.path.join(BASE_DIR, "apple_products_pricing_engineered.csv")

# Low-cardinality nominal columns -> One-Hot Encoding (no inherent order)
ONE_HOT_COLS = ["Platform", "Condition", "Stock_Status", "Sale_Event"]

# Higher-cardinality columns -> Label Encoding (keeps the feature space
# compact; tree-based models handle the resulting integer codes fine)
LABEL_ENCODE_COLS = ["Product_Category", "Model_Name"]

NUMERIC_COLS = ["Launch_Price_USD", "Current_Price_USD", "Discount_Pct", "Rating", "Reviews_Count"]


def load_cleaned(path=CLEANED_PATH):
    return pd.read_csv(path, parse_dates=["Date"])


def identify_categorical_features(df):
    print("=" * 70)
    print("1. Categorical Feature Identification")
    print("=" * 70)
    cat_cols = df.select_dtypes(include="object").columns.tolist()
    for c in cat_cols:
        print(f"{c:20s} -> {df[c].nunique()} unique values: {sorted(df[c].unique())[:8]}{' ...' if df[c].nunique() > 8 else ''}")
    print(
        "\nDecision: Platform, Condition, Stock_Status, Sale_Event are "
        "low-cardinality and nominal -> One-Hot Encoding.\n"
        "Product_Category and Model_Name have more unique values -> Label "
        "Encoding, to avoid an explosion of one-hot columns.\n"
    )
    return cat_cols


def apply_one_hot_encoding(df):
    print("=" * 70)
    print("2. One-Hot Encoding")
    print("=" * 70)
    df = df.copy()
    before_cols = df.shape[1]
    df = pd.get_dummies(df, columns=ONE_HOT_COLS, prefix=ONE_HOT_COLS)
    after_cols = df.shape[1]
    print(f"Columns before: {before_cols}, after one-hot encoding {ONE_HOT_COLS}: {after_cols}")
    new_cols = [c for c in df.columns if any(c.startswith(p + "_") for p in ONE_HOT_COLS)]
    print("New one-hot columns:", new_cols)
    print()
    return df


def apply_label_encoding(df):
    print("=" * 70)
    print("3. Label Encoding")
    print("=" * 70)
    df = df.copy()
    encoders = {}
    for col in LABEL_ENCODE_COLS:
        le = LabelEncoder()
        df[col + "_Encoded"] = le.fit_transform(df[col])
        encoders[col] = le
        mapping = dict(zip(le.classes_, le.transform(le.classes_)))
        print(f"{col} -> {col}_Encoded, mapping (first 5): {dict(list(mapping.items())[:5])}")
    print()
    return df, encoders


def apply_scaling(df):
    print("=" * 70)
    print("4. Normalization / Standardization")
    print("=" * 70)
    df = df.copy()
    scaler = StandardScaler()
    scaled_cols = [c + "_Scaled" for c in NUMERIC_COLS]
    df[scaled_cols] = scaler.fit_transform(df[NUMERIC_COLS])

    print("Applied StandardScaler (zero mean, unit variance) to:", NUMERIC_COLS)
    print(df[scaled_cols].describe().loc[["mean", "std"]])
    print(
        "\nImportance: Launch_Price_USD/Current_Price_USD (0-2000) and "
        "Reviews_Count (0-11000+) live on very different scales than "
        "Rating (3.8-4.9) or Discount_Pct (0-80). Distance- and "
        "gradient-based algorithms (KNN, SVM, PCA, linear/logistic "
        "regression, neural nets) would let the large-magnitude columns "
        "dominate the loss/distance unless every numeric feature is put "
        "on a comparable scale first.\n"
    )
    return df


def main():
    df = load_cleaned()
    identify_categorical_features(df)
    df = apply_one_hot_encoding(df)
    df, _ = apply_label_encoding(df)
    df = apply_scaling(df)

    print("=" * 70)
    print("5. Final Engineered Dataset")
    print("=" * 70)
    print(f"Final shape: {df.shape}")
    print("Columns:", df.columns.tolist())

    df.to_csv(ENGINEERED_PATH, index=False)
    print(f"\nEngineered dataset saved to: {ENGINEERED_PATH}")


if __name__ == "__main__":
    main()
