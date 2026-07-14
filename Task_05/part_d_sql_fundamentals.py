"""
Task 05 - Part D: SQL Fundamentals with Python (25 Marks)
1. Create a small relational database from the cleaned dataset.
2. Perform SELECT, WHERE, GROUP BY, and JOIN queries.
3. Connect Python to the database and display query results.
"""

import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
CLEANED_PATH = os.path.join(BASE_DIR, "apple_products_pricing_cleaned.csv")
DB_PATH = os.path.join(BASE_DIR, "apple_products_pricing.db")


def build_database(df, db_path=DB_PATH):
    print("=" * 70)
    print("1. Build Relational Database")
    print("=" * 70)

    if os.path.exists(db_path):
        os.remove(db_path)
    conn = sqlite3.connect(db_path)

    # products: one row per distinct Model_Name (dimension table)
    products = (
        df[["Model_Name", "Product_Category", "Launch_Price_USD"]]
        .drop_duplicates(subset="Model_Name")
        .reset_index(drop=True)
    )
    products.insert(0, "product_id", products.index + 1)

    # sales: one row per listing observation (fact table), referencing
    # products via a foreign key so a JOIN is meaningful
    sales = df.merge(
        products[["product_id", "Model_Name"]], on="Model_Name", how="left"
    )
    sales = sales[
        [
            "product_id",
            "Date",
            "Platform",
            "Condition",
            "Current_Price_USD",
            "Discount_Pct",
            "Sale_Event",
            "Stock_Status",
            "Rating",
            "Reviews_Count",
        ]
    ].reset_index(drop=True)
    sales.insert(0, "sale_id", sales.index + 1)

    products.to_sql("products", conn, if_exists="replace", index=False)
    sales.to_sql("sales", conn, if_exists="replace", index=False)

    conn.execute("CREATE INDEX idx_sales_product_id ON sales(product_id)")
    conn.commit()

    print(f"Created table 'products' ({len(products)} rows) - Model_Name, Product_Category, Launch_Price_USD")
    print(f"Created table 'sales' ({len(sales)} rows) - references products.product_id as a foreign key")
    print(f"Database saved to: {db_path}\n")
    return conn


def run_select(conn):
    print("=" * 70)
    print("2. SELECT - sample listing records")
    print("=" * 70)
    q = "SELECT sale_id, product_id, Date, Platform, Current_Price_USD, Discount_Pct FROM sales LIMIT 5;"
    print(q)
    print(pd.read_sql_query(q, conn))
    print()


def run_where(conn):
    print("=" * 70)
    print("3. WHERE - out-of-stock iPhone listings on Amazon")
    print("=" * 70)
    q = """
        SELECT s.sale_id, p.Model_Name, s.Platform, s.Stock_Status, s.Current_Price_USD
        FROM sales s
        JOIN products p ON p.product_id = s.product_id
        WHERE p.Product_Category = 'iPhone'
          AND s.Platform = 'Amazon'
          AND s.Stock_Status = 'Out of Stock'
        LIMIT 5;
    """
    print(q)
    print(pd.read_sql_query(q, conn))
    print()


def run_group_by(conn):
    print("=" * 70)
    print("4. GROUP BY - average discount and listing count per platform")
    print("=" * 70)
    q = """
        SELECT Platform,
               COUNT(*) AS listing_count,
               ROUND(AVG(Discount_Pct), 2) AS avg_discount_pct,
               ROUND(AVG(Current_Price_USD), 2) AS avg_current_price
        FROM sales
        GROUP BY Platform
        ORDER BY avg_discount_pct DESC;
    """
    print(q)
    print(pd.read_sql_query(q, conn))
    print()


def run_join(conn):
    print("=" * 70)
    print("5. JOIN - average current price per category (products JOIN sales)")
    print("=" * 70)
    q = """
        SELECT p.Product_Category,
               COUNT(s.sale_id) AS listing_count,
               ROUND(AVG(p.Launch_Price_USD), 2) AS avg_launch_price,
               ROUND(AVG(s.Current_Price_USD), 2) AS avg_current_price,
               ROUND(AVG(s.Rating), 2) AS avg_rating
        FROM products p
        JOIN sales s ON s.product_id = p.product_id
        GROUP BY p.Product_Category
        ORDER BY avg_current_price DESC;
    """
    print(q)
    print(pd.read_sql_query(q, conn))
    print()


def main():
    df = pd.read_csv(CLEANED_PATH, parse_dates=["Date"])
    conn = build_database(df)
    try:
        run_select(conn)
        run_where(conn)
        run_group_by(conn)
        run_join(conn)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
