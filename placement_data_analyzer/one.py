"""
Placement Data Analyzer
PS No. 23 | BCA First Semester, Section 1C

This program reads campus placement records from placement.csv.
It shows placement statistics, branch-wise details and students
whose package is above a limit entered by the user.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import math

FILE_NAME = "placement.csv"
COLUMNS = ["Student", "Branch", "Company", "Package_LPA"]


def load_placement_data():
    """Read the CSV file and remove rows with invalid or duplicate data."""
    file_path = Path(__file__).parent / FILE_NAME

    if not file_path.exists():
        print(f"File '{FILE_NAME}' was not found.")
        return pd.DataFrame(columns=COLUMNS)

    try:
        data = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        print("The placement file is empty.")
        return pd.DataFrame(columns=COLUMNS)
    except Exception as error:
        print("Could not read the CSV file:", error)
        return pd.DataFrame(columns=COLUMNS)

    missing_columns = [column for column in COLUMNS if column not in data.columns]
    if missing_columns:
        print("CSV is missing required columns:", ", ".join(missing_columns))
        return pd.DataFrame(columns=COLUMNS)

    valid_rows = []

    for index, row in data.iterrows():
        row_number = index + 1
        student = str(row["Student"]).strip()
        branch = str(row["Branch"]).strip()
        company = str(row["Company"]).strip()

        try:
            package = float(row["Package_LPA"])
        except (ValueError, TypeError):
            print(f"Row {row_number} skipped: invalid Package '{row['Package_LPA']}'.")
            continue

        if not student or not branch or not company:
            print(f"Row {row_number} skipped: student, branch and company are required.")
            continue

        if not math.isfinite(package):
            print(f"Row {row_number} skipped: invalid Package '{row['Package_LPA']}'.")
            continue

        if package <= 0:
            print(f"Row {row_number} skipped: Package must be positive.")
            continue

        valid_rows.append({
            "Student": student,
            "Branch": branch,
            "Company": company,
            "Package_LPA": package
        })

    clean_data = pd.DataFrame(valid_rows, columns=COLUMNS)

    before_count = len(clean_data)
    clean_data = clean_data.drop_duplicates()
    duplicate_count = before_count - len(clean_data)

    if duplicate_count:
        print(f"Duplicate rows removed: {duplicate_count}")

    return clean_data


def show_summary(data):
    """Display total placed students, average package and highest package."""
    if data.empty:
        print("No valid placement records are available.")
        return

    total_placed = len(data)
    average_package = data["Package_LPA"].mean()
    highest_row = data.loc[data["Package_LPA"].idxmax()]

    print("\nPLACEMENT SUMMARY")
    print("-----------------")
    print(f"Total placed: {total_placed}")
    print(f"Average package: {average_package:.2f} LPA")
    print(
        f"Highest: {highest_row['Package_LPA']:.2f} LPA "
        f"({highest_row['Student']}, {highest_row['Company']})"
    )


def show_branch_analysis(data):
    """Show branch-wise placements and students above a package limit."""
    if data.empty:
        print("No valid placement records are available.")
        return

    try:
        package_limit = float(input("Enter package limit in LPA: "))
        if package_limit < 0:
            print("Package limit cannot be negative.")
            return
    except ValueError:
        print("Invalid limit. Please enter a number.")
        return

    branch_counts = data.groupby("Branch")["Student"].count()
    branch_averages = data.groupby("Branch")["Package_LPA"].mean()

    print("\nBRANCH-WISE PLACEMENTS")
    print("----------------------")
    count_text = " | ".join(
        f"{branch}: {count}" for branch, count in branch_counts.items()
    )
    print("Placements:", count_text)

    average_text = " | ".join(
        f"{branch} {average:.2f}" for branch, average in branch_averages.items()
    )
    print("Average package:", average_text)

    above_limit = data[data["Package_LPA"] > package_limit]
    if above_limit.empty:
        print(f"Above {package_limit:g} LPA: No students found")
    else:
        student_text = " | ".join(
            f"{row.Student} ({row.Package_LPA:.2f})"
            for row in above_limit.itertuples()
        )
        print(f"Above {package_limit:g} LPA:", student_text)

    # Bar chart: number of placed students in each branch
    plt.figure(figsize=(7, 4))
    branch_counts.plot(kind="bar")
    plt.title("Branch-wise Placements")
    plt.xlabel("Branch")
    plt.ylabel("Number of Students")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    # Pie chart: share of placements by branch
    plt.figure(figsize=(6, 6))
    branch_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Branch-wise Placements")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


def main():
    print("=" * 42)
    print("          PLACEMENT DATA ANALYZER")
    print("=" * 42)

    data = load_placement_data()

    while True:
        print("\n1. Placement Summary")
        print("2. Branch-wise Analysis and Package Filter")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_summary(data)
        elif choice == "2":
            show_branch_analysis(data)
        elif choice == "3":
            print("Thank you for using Placement Data Analyzer.")
            break
        else:
            print("Invalid choice. Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()
