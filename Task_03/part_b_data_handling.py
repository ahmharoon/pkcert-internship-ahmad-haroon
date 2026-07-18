"""
Task 03 - Part B: Python for Data Handling (25 Marks)
1. Read, write, append text files
2. Exception handling
3. Read and display data from CSV and JSON files
"""

import csv
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "sample_data")
os.makedirs(DATA_DIR, exist_ok=True)

TEXT_FILE = os.path.join(DATA_DIR, "notes.txt")
CSV_FILE = os.path.join(DATA_DIR, "students.csv")
JSON_FILE = os.path.join(DATA_DIR, "students.json")


# ---------------------------------------------------------------------------
# 1. Read, write, and append text files
# ---------------------------------------------------------------------------
def demonstrate_text_files():
    print("=" * 60)
    print("1. Text File Read / Write / Append")
    print("=" * 60)

    # Write (overwrites the file)
    with open(TEXT_FILE, "w") as f:
        f.write("PKCERT AI & Software Development Internship\n")
        f.write("Task 03 - Data Handling\n")

    # Append (adds a line without erasing existing content)
    with open(TEXT_FILE, "a") as f:
        f.write("This line was appended.\n")

    # Read
    with open(TEXT_FILE, "r") as f:
        content = f.read()

    print(f"Contents of {os.path.basename(TEXT_FILE)}:")
    print(content)


# ---------------------------------------------------------------------------
# 2. Exception handling
# ---------------------------------------------------------------------------
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"Error: cannot divide {a} by zero.")
        return None
    except TypeError:
        print(f"Error: unsupported types for division ({type(a)}, {type(b)}).")
        return None
    else:
        print(f"{a} / {b} = {result}")
        return result
    finally:
        print("-> safe_divide() attempt finished.")


def safe_read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: file not found -> {path}")
        return None


def demonstrate_exception_handling():
    print("=" * 60)
    print("2. Exception Handling")
    print("=" * 60)

    safe_divide(10, 2)
    safe_divide(10, 0)
    safe_divide(10, "two")
    safe_read_file(os.path.join(DATA_DIR, "does_not_exist.txt"))
    print()


# ---------------------------------------------------------------------------
# 3. Read and display data from CSV and JSON files
# ---------------------------------------------------------------------------
def create_sample_csv():
    rows = [
        {"name": "Ahmad", "age": 21, "major": "AI"},
        {"name": "Fatima", "age": 22, "major": "Data Science"},
        {"name": "Bilal", "age": 20, "major": "Software Engineering"},
    ]
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "major"])
        writer.writeheader()
        writer.writerows(rows)


def create_sample_json():
    data = {
        "cohort": "PKCERT-2026",
        "students": [
            {"name": "Ahmad", "age": 21, "major": "AI"},
            {"name": "Fatima", "age": 22, "major": "Data Science"},
        ],
    }
    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=2)


def demonstrate_csv_json():
    print("=" * 60)
    print("3. Reading CSV and JSON Files")
    print("=" * 60)

    create_sample_csv()
    create_sample_json()

    print(f"--- {os.path.basename(CSV_FILE)} ---")
    with open(CSV_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

    print(f"\n--- {os.path.basename(JSON_FILE)} ---")
    with open(JSON_FILE, "r") as f:
        data = json.load(f)
    print("Cohort:", data["cohort"])
    for student in data["students"]:
        print(f"  {student['name']} ({student['age']}) - {student['major']}")
    print()


if __name__ == "__main__":
    demonstrate_text_files()
    demonstrate_exception_handling()
    demonstrate_csv_json()
