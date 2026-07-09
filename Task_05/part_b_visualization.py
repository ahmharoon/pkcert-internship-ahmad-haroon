"""
Task 05 - Part B: Data Visualization (25 Marks)
1. Histogram, Boxplot, Correlation Heatmap, and two additional visualizations
   using Matplotlib and Seaborn.
2. Insights obtained from each visualization.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = os.path.dirname(__file__)
CLEANED_PATH = os.path.join(BASE_DIR, "apple_products_pricing_cleaned.csv")
VIS_DIR = os.path.join(BASE_DIR, "visualizations")

sns.set_theme(style="whitegrid")


def load_cleaned(path=CLEANED_PATH):
    df = pd.read_csv(path, parse_dates=["Date"])
    return df


def plot_histogram(df):
    print("=" * 70)
    print("1. Histogram - Current Price Distribution")
    print("=" * 70)
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Current_Price_USD"], bins=40, kde=True, color="#4C72B0")
    plt.title("Distribution of Current Selling Price (USD)")
    plt.xlabel("Current Price (USD)")
    plt.ylabel("Count")
    plt.tight_layout()
    out = os.path.join(VIS_DIR, "1_histogram_current_price.png")
    plt.savefig(out, dpi=120)
    plt.close()
    print(f"Saved: {out}")
    print(
        "Insight: prices cluster into distinct bands (Watch/iPad at the low "
        "end, iPhone in the middle, MacBook at the high end), giving the "
        "distribution several peaks rather than a single bell shape - a "
        "sign that Product_Category is a strong price driver.\n"
    )


def plot_boxplot(df):
    print("=" * 70)
    print("2. Boxplot - Current Price by Product Category")
    print("=" * 70)
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="Product_Category", y="Current_Price_USD", palette="Set2")
    plt.title("Current Price by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Current Price (USD)")
    plt.tight_layout()
    out = os.path.join(VIS_DIR, "2_boxplot_price_by_category.png")
    plt.savefig(out, dpi=120)
    plt.close()
    print(f"Saved: {out}")
    print(
        "Insight: Mac has the highest median price and widest spread, "
        "Watch the lowest and tightest; iPhone and iPad show a handful of "
        "high-end outliers (Pro/Max configurations) above their main "
        "price band.\n"
    )


def plot_correlation_heatmap(df):
    print("=" * 70)
    print("3. Correlation Heatmap - Numeric Features")
    print("=" * 70)
    numeric_cols = ["Launch_Price_USD", "Current_Price_USD", "Discount_Pct", "Rating", "Reviews_Count"]
    corr = df[numeric_cols].corr()
    plt.figure(figsize=(7, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    out = os.path.join(VIS_DIR, "3_correlation_heatmap.png")
    plt.savefig(out, dpi=120)
    plt.close()
    print(f"Saved: {out}")
    print(corr)
    print(
        "\nInsight: Launch_Price_USD and Current_Price_USD are strongly "
        "positively correlated (as expected - resale price tracks launch "
        "price), while Discount_Pct correlates negatively with "
        "Current_Price_USD (bigger discounts push the current price down "
        "relative to launch). Rating and Reviews_Count show little "
        "correlation with price, suggesting pricing is driven mainly by "
        "product tier, not popularity.\n"
    )


def plot_avg_discount_by_platform(df):
    print("=" * 70)
    print("4. Bar Chart - Average Discount % by Platform and Category")
    print("=" * 70)
    pivot = df.groupby(["Product_Category", "Platform"])["Discount_Pct"].mean().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(data=pivot, x="Product_Category", y="Discount_Pct", hue="Platform", palette="Set1")
    plt.title("Average Discount % by Category and Platform")
    plt.xlabel("Product Category")
    plt.ylabel("Average Discount (%)")
    plt.tight_layout()
    out = os.path.join(VIS_DIR, "4_bar_avg_discount_platform.png")
    plt.savefig(out, dpi=120)
    plt.close()
    print(f"Saved: {out}")
    print(pivot)
    print(
        "\nInsight: average discounts are broadly similar across Amazon and "
        "Flipkart for the same category, with Watch and iPad typically "
        "seeing slightly larger average discounts than iPhone and Mac.\n"
    )


def plot_price_trend_over_time(df):
    print("=" * 70)
    print("5. Line Chart - Average Price Trend Over Time by Category")
    print("=" * 70)
    trend = (
        df.set_index("Date")
        .groupby("Product_Category")["Current_Price_USD"]
        .resample("Q")
        .mean()
        .reset_index()
    )
    plt.figure(figsize=(9, 5))
    sns.lineplot(data=trend, x="Date", y="Current_Price_USD", hue="Product_Category")
    plt.title("Average Current Price Over Time by Category (Quarterly)")
    plt.xlabel("Date")
    plt.ylabel("Average Current Price (USD)")
    plt.tight_layout()
    out = os.path.join(VIS_DIR, "5_line_price_trend.png")
    plt.savefig(out, dpi=120)
    plt.close()
    print(f"Saved: {out}")
    print(
        "Insight: average prices per category are fairly stable over time "
        "with periodic dips that line up with sale events (e.g. Black "
        "Friday, Big Billion Days), rather than a steady long-term decline "
        "or rise.\n"
    )


def main():
    os.makedirs(VIS_DIR, exist_ok=True)
    df = load_cleaned()
    plot_histogram(df)
    plot_boxplot(df)
    plot_correlation_heatmap(df)
    plot_avg_discount_by_platform(df)
    plot_price_trend_over_time(df)
    print("All visualizations saved to:", VIS_DIR)


if __name__ == "__main__":
    main()
