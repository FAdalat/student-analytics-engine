::: {align="center"}
# 🎓 Student Analytics Engine

### A lightweight Python CLI application for managing students and analysing exam results.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-6C757D?style=for-the-badge)

**Manage student records. Track exam results. Calculate averages. Rank
performance.**
:::

------------------------------------------------------------------------

## 📌 Overview

**Student Analytics Engine** is a command-line application written in
Python. It helps manage student records and provides simple analysis of
exam performance.

Student information and exam results are stored locally in a JSON file,
so records remain available between program runs.

## ✨ Features

  -----------------------------------------------------------------------
  Feature                             Description
  ----------------------------------- -----------------------------------
  ➕ Add students                     Register a student with an ID, name
                                      and exam results

  🔎 View records                     Find and display a student using
                                      their ID

  ✏️ Edit records                     Update a student's name or exam
                                      results

  🗑️ Remove students                  Delete a student record after
                                      confirmation

  📊 Calculate averages               Calculate an individual student's
                                      average exam result

  🏆 Student ranking                  Sort students by average result,
                                      from highest to lowest

  💾 JSON persistence                 Save and load student records using
                                      `data.json`
  -----------------------------------------------------------------------

## 🛠️ Built With

-   **Python** --- application logic and data processing
-   **JSON** --- local data storage
-   **Python standard library** --- no third-party packages required

## 🚀 Getting Started

### 1. Clone the repository

``` bash
git clone https://github.com/YOUR-USERNAME/student-analytics-engine.git
```

### 2. Open the project directory

``` bash
cd student-analytics-engine
```

### 3. Project structure

``` text
student-analytics-engine/
│
├── main.py       # Main application
├── data.json     # Student records and exam results
└── README.md     # Project documentation
```

### 4. Run the application

Make sure Python 3 is installed, then run:

``` bash
python main.py
```

On some systems, use:

``` bash
python3 main.py
```

> **Important:** Run the command from the project directory so the
> application can find `data.json`.

## 💻 How to Use

When the application starts, enter one of the available actions:

  Action      What it does
  ----------- -------------------------------
  `add`       Add a new student
  `view`      View a student's record
  `edit`      Edit an existing student
  `remove`    Remove a student
  `average`   Calculate a student's average
  `ranking`   Display the student ranking
  `exit`      Close the application

### Example workflow

``` text
Enter action: add

Enter student ID: STU-004
Enter student name: Murad
Enter number of exam results: 3
Enter exam result: 87
Enter exam result: 91
Enter exam result: 84
```

The application calculates the average when requested:

``` text
Average exam result for Murad: 87.33333333333333
```

## 🗂️ Data Format

Student records are stored in `data.json`.

Example:

``` json
{
    "students": [
        {
            "id": "STU-001",
            "name": "Ali",
            "exam results": [85, 90, 78]
        },
        {
            "id": "STU-002",
            "name": "Cavid",
            "exam results": [88, 92, 81]
        }
    ]
}
```

Each student record contains:

-   `id` --- student identifier
-   `name` --- student name
-   `exam results` --- list of exam scores

Keep the JSON structure valid when editing the file manually.

## 🧠 What This Project Practises

-   Variables, data types and user input
-   Conditional statements and loops
-   Functions and modular program structure
-   Lists and dictionaries
-   Searching and sorting
-   Working with files
-   Reading and writing JSON data
-   Basic data analysis

## 🔭 Possible Future Improvements

-   Stronger input validation and error handling
-   Automated unit tests with `pytest`
-   Search and filtering options
-   Exporting reports
-   A graphical user interface
-   Migration from JSON storage to SQLite

## 👨‍💻 Author

**Adalat Farajov**

Artificial Intelligence Systems student at Vilnius Tech.

------------------------------------------------------------------------

::: {align="center"}
*Built as a hands-on Python project to strengthen programming
fundamentals.*
:::
