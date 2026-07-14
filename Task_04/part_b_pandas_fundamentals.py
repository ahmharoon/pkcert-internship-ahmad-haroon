"""
Task 04 - Part B: Pandas Fundamentals (30 Marks)
1. Series and DataFrame creation/manipulation
2. Indexing, filtering, sorting, selection
3. Groupby operations
4. Merge and join
"""

import pandas as pd


# ---------------------------------------------------------------------------
# 1. Series and DataFrame creation and manipulation
# ---------------------------------------------------------------------------
def demonstrate_series_dataframe():
    print("=" * 60)
    print("1. Series & DataFrame Creation / Manipulation")
    print("=" * 60)

    series = pd.Series([100, 85, 92, 78], index=["Ahmad", "Fatima", "Bilal", "Sara"], name="score")
    print("Series:\n", series)

    df = pd.DataFrame({
        "name": ["Ahmad", "Fatima", "Bilal", "Sara", "Hina"],
        "age": [21, 22, 20, 23, 21],
        "department": ["AI", "Data Science", "AI", "Software Eng", "Data Science"],
        "score": [88, 92, 79, 95, 84],
    })
    print("\nDataFrame:\n", df)

    df["passed"] = df["score"] >= 80  # add a derived column
    df.loc[len(df)] = ["Usman", 24, "AI", 70, False]  # add a row
    print("\nDataFrame after adding 'passed' column and a new row:\n", df)
    print()
    return df


# ---------------------------------------------------------------------------
# 2. Indexing, filtering, sorting, selection
# ---------------------------------------------------------------------------
def demonstrate_indexing_filtering_sorting(df):
    print("=" * 60)
    print("2. Indexing, Filtering, Sorting, Selection")
    print("=" * 60)

    print("Select 'name' and 'score' columns:\n", df[["name", "score"]])
    print("\nRow at index 2 (iloc):\n", df.iloc[2])
    print("\nRows where department == 'AI':\n", df[df["department"] == "AI"])
    print("\nRows where score >= 85 AND passed:\n", df[(df["score"] >= 85) & (df["passed"])])
    print("\nSorted by score (descending):\n", df.sort_values("score", ascending=False))
    print()


# ---------------------------------------------------------------------------
# 3. Groupby operations
# ---------------------------------------------------------------------------
def demonstrate_groupby(df):
    print("=" * 60)
    print("3. Groupby Operations")
    print("=" * 60)

    grouped = df.groupby("department")["score"].agg(["mean", "min", "max", "count"])
    print("Score summary by department:\n", grouped)

    pass_rate = df.groupby("department")["passed"].mean()
    print("\nPass rate by department:\n", pass_rate)
    print()


# ---------------------------------------------------------------------------
# 4. Merge and join
# ---------------------------------------------------------------------------
def demonstrate_merge_join():
    print("=" * 60)
    print("4. Merge and Join")
    print("=" * 60)

    students = pd.DataFrame({
        "student_id": [1, 2, 3, 4],
        "name": ["Ahmad", "Fatima", "Bilal", "Sara"],
    })
    grades = pd.DataFrame({
        "student_id": [1, 2, 3, 5],
        "grade": ["A", "A+", "B", "A"],
    })

    print("students:\n", students)
    print("\ngrades:\n", grades)

    inner = pd.merge(students, grades, on="student_id", how="inner")
    print("\nINNER merge (only matching student_ids):\n", inner)

    left = pd.merge(students, grades, on="student_id", how="left")
    print("\nLEFT merge (all students, grade=NaN if missing):\n", left)

    outer = pd.merge(students, grades, on="student_id", how="outer")
    print("\nOUTER merge (union of both, NaN where no match):\n", outer)

    joined = students.set_index("student_id").join(grades.set_index("student_id"), how="left")
    print("\nDataFrame.join() equivalent (index-based left join):\n", joined)

    print(
        "\nExplanation: inner keeps only rows present in both frames; left keeps "
        "every row from the left frame filling unmatched right-side values with "
        "NaN; outer keeps the union of both, filling gaps on either side with "
        "NaN. join() is a convenience method for merging on the index instead "
        "of an explicit key column."
    )
    print()


if __name__ == "__main__":
    df = demonstrate_series_dataframe()
    demonstrate_indexing_filtering_sorting(df)
    demonstrate_groupby(df)
    demonstrate_merge_join()
