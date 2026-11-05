# Placement Data Analyzer

**PS No.:** 23  
**Course:** Programming Fundamentals Using Python  
**Semester/Section:** BCA First Semester, 1C  
**Student:** Dhananjay Sahu

## 1. Project overview
Placement Data Analyzer is a small Python console program that reads campus placement records from a CSV file. It summarizes the placement data and compares placements across branches.

## 2. Objectives
- Read placement records from a CSV file.
- Calculate the total number of placed students, average package and highest package.
- Find branch-wise placement counts and average packages.
- Display students whose package is above a limit entered by the user.
- Show the results using bar and pie charts.

## 3. Features
- CSV input through `placement.csv`.
- Checks package values and skips non-numeric or non-positive packages.
- Skips rows with missing student, branch or company names.
- Removes exact duplicate records.
- Displays placement summary.
- Uses Pandas `groupby()` and boolean filtering.
- Creates Matplotlib bar and pie charts.

## 4. Requirements
- Python 3
- pandas
- matplotlib

Install the libraries from a terminal:

```bash
python -m pip install pandas matplotlib
```

## 5. Project files
```text
Placement_Data_Analyzer/
│
├── one.py
├── README.md
├── placement.csv
├── test_data/
│   ├── test_case_1.csv
│   ├── test_case_2.csv
│   ├── test_case_3.csv
│   └── test_case_4.csv
└── Test_cases_passed.pdf
```

## 6. How to run
1. Keep `one.py` and `placement.csv` in the same folder.
2. Open a terminal in that folder.
3. Install the required libraries if they are not already installed.
4. Run:

```bash
python one.py
```

5. Select `1` for the placement summary.
6. Select `2` for branch-wise analysis. Enter a package limit when asked.
7. Select `3` to close the program.

## 7. Input format
The CSV file must contain these columns:

| Column | Meaning |
|---|---|
| Student | Student name |
| Branch | Student's branch |
| Company | Company name |
| Package_LPA | Package in lakhs per annum |

Example:

```csv
Student,Branch,Company,Package_LPA
Aman,CSE,TCS,6
Riya,CSE,Infosys,8
Karan,ECE,Wipro,4
```

## 8. Output
The program displays:
- Total placed students.
- Average package in LPA.
- Highest package with student and company.
- Number of placements in each branch.
- Average package for each branch.
- Students above the entered package limit.

It also opens a bar chart and a pie chart for branch-wise placements.

## 9. Test cases
The project description provides four test cases:
1. Normal input: three placement records.
2. Boundary input: one placement record.
3. Invalid input: a non-numeric package and a negative package are skipped.
4. Different valid scenario: branch-wise analysis and students above 7 LPA.

The sample CSV files for these cases are available in the `test_data` folder. To run a test, copy the required test CSV into the project folder and rename it to `placement.csv`.

## 10. Concepts used
- Functions
- Conditional statements and loops
- CSV file handling through Pandas
- DataFrame operations
- `groupby()` for branch-wise analysis
- Boolean filtering
- Matplotlib charts
- Input validation

## 11. Note
The records supplied with this project are dummy data for demonstrating the program. They are not actual college placement records.
