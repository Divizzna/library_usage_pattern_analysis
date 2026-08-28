# 📚 Library Usage Pattern Analysis

A Python-based mini project that analyzes library usage patterns and
generates reports and visualizations from library visit data.

## 🎯 Project Overview

This project analyzes student library usage data to identify reading
interests, visit patterns, and book-category preferences.

It uses data collected through a Google Sheet and processes the
information with Python to generate useful reports and charts.

## ✨ Features

-   📊 Analyzes library usage and visit patterns
-   📚 Identifies students' interested topics
-   🔎 Provides book recommendations based on interests
-   📈 Generates visual reports and charts
-   📁 Saves generated reports and graphs in a dedicated `reports`
    folder
-   🧮 Uses Python data analysis libraries for processing

## 🛠️ Technologies Used

-   **Python**
-   **Pandas** -- data processing and analysis
-   **Matplotlib** -- data visualization
-   **Requests** -- retrieving data
-   **Google Sheets** -- source of library usage data

## 📂 Project Structure

``` text
library_usage_pattern/
│
├── reports/
│   ├── book_category_chart.png
│   ├── department_chart.png
│   ├── purpose_pie_chart.png
│   └── usn_frequency_report.csv
│
└── library_analysis.py
```

## ⚙️ How It Works

1.  Library usage data is collected from a Google Sheet.
2.  The Python program reads and processes the data.
3.  Usage patterns and interests are analyzed.
4.  Book recommendations are generated for identified interests.
5.  Charts and CSV reports are created automatically.
6.  The generated files are stored in the `reports` folder.

## ▶️ How to Run

### 1. Clone the repository

``` bash
git clone https://github.com/Divizzna/library_usage_pattern_analysis.git
cd library_usage_pattern_analysis/library_usage_pattern
```

### 2. Install the required Python packages

``` bash
pip install pandas matplotlib requests
```

### 3. Run the analysis

``` bash
python library_analysis.py
```

After successful execution, check the `reports` folder for the generated
charts and CSV report.

## 📊 Generated Reports

The project currently generates:

-   **Book Category Chart** -- visualization of book/category usage
-   **Department Chart** -- visualization based on student departments
-   **Purpose Pie Chart** -- visualization of library visit purposes
-   **USN Frequency Report** -- CSV report containing usage frequency
    information

## 💡 Example Output

The program can identify a student's total library visits and interested
topics, then provide book recommendations based on those interests.

## 🚀 Future Improvements

-   Add an interactive dashboard
-   Add more detailed usage analytics
-   Improve recommendation accuracy
-   Add filtering by date, department, and book category
-   Deploy the project as a web application

## 👩‍💻 Author
**Divizzna**

GitHub: https://github.com/Divizzna
