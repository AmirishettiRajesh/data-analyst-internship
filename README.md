# Data Science Fundamentals Assessment

**Internship task:** Task 1, Data Analyst Internship  
**Internship duration:** 02-Oct-2026 to 27-Nov-2026

## Objectives

- Demonstrate core Python, data type, and data structure knowledge.
- Apply statistical foundations to a small dataset.
- Practice NumPy, Pandas, and common data visualizations.
- Demonstrate reproducible, validated, privacy-aware analysis.

## Project overview

This beginner-friendly project analyzes a reproducible, fictional student-performance CSV. The Python script is the executable entry point: it validates and loads the root-level CSV, calculates summaries, creates six figures, writes `outputs/results.txt`, and builds the Word report from calculated results. The Jupyter notebook contains the same workflow with Markdown explanations. No external dataset or source is used.

All records, including names and IDs, are fictional and created only for this exercise. This sample is intentionally small and hand-authored, so findings are illustrative and should not be generalized to real students.

## Technologies used

- Python 3.10 or newer (tested in Python 3.11)
- NumPy, Pandas
- Matplotlib, Seaborn
- Jupyter Notebook
- python-docx

## Installation

Open a terminal in this project folder. Optionally create and activate a virtual environment, then install dependencies:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS/Linux, activate with `source .venv/bin/activate`. If `py` is unavailable on Windows, use `python` to create the virtual environment.

## How to run

From this folder, run the end-to-end analysis:

```powershell
python fundamentals.py
```

The script reads and validates the supplied root-level `student_performance.csv` without overwriting it. If that file is absent, it creates it from the fixed sample records. Each run writes `outputs/results.txt`, six PNG files in `outputs/charts/`, and `report/Task_1_Data_Science_Fundamentals_Report.docx`. Required columns, types, missing values, identifier uniqueness, plausible ranges, and score bounds are validated.

To use the notebook, open `fundamentals.ipynb` in VS Code with the Jupyter extension or launch Jupyter from this folder:

```powershell
jupyter notebook fundamentals.ipynb
```

Select the environment where `requirements.txt` was installed, then use **Run All**. Notebook cells resolve files relative to this project folder and create the same CSV, figures, and report. Run the script first if the report and figures are needed before using the notebook.

## Project structure

```text
Task-1-Data-Science-Fundamentals/
├── fundamentals.py
├── fundamentals.ipynb
├── student_performance.csv
├── README.md
├── requirements.txt
├── report/
│   └── Task_1_Data_Science_Fundamentals_Report.docx
└── outputs/
    ├── results.txt
    └── charts/
        └── *.png                     # six generated figures
```

## Topics covered

- **Python:** variables; integer, float, string, Boolean; conversion; arithmetic/comparison/logical operators; conditionals; `for`/`while`; functions; lists, tuples, sets, dictionaries; `try`/`except`; context-managed CSV file handling.
- **Statistics:** mean, median, mode, minimum, maximum, range, sample variance and standard deviation, 25th/75th percentiles, and Pearson correlation.
- **NumPy:** 1D/2D arrays, indexing, slicing, arithmetic, reshape, mean/minimum/maximum, and sample standard deviation.
- **Pandas:** DataFrame creation and CSV loading, `head()`, `tail()`, `shape`, `info()`, `describe()`, selection, filtering, sorting, grouping, aggregation, missing values, and duplicates.
- **Visualization:** bar chart, line chart, histogram, scatter plot, box plot, and correlation heatmap.
- **Best practices:** cleaning, validation, missing-value and duplicate handling, data types, reproducibility, readable names, comments, docstrings, privacy, clear axes, and responsible interpretation.

## Results and observations

The fixed sample contains 20 fictional records and 8 fields. Calculated from the current records, Exam_Score has mean 78.10, median 77.50, mode 75, and range 38 (58 to 96); sample standard deviation is 10.75. The Study_Hours/Exam_Score Pearson correlation is 0.994. The unusually strong association reflects this deliberately constructed teaching sample, not a real-world estimate. Interpret all relationships as descriptive only: the sample is small, and correlation does not demonstrate causation. The script prints the schema, preview, numeric description, group means, NumPy reductions, and data-quality demonstration, then writes six charts and uses calculated values in the DOCX report.

The script also reports group counts and score summaries, cleaning counts, and outlier flags in `outputs/results.txt`. All numbers are calculated from the included CSV.

## Best practices

Validate data before analysis, preserve the original when demonstrating imputation, document cleaning choices, use meaningful names and comments, and keep dependencies and input records explicit for reproducibility. Protect student privacy, label units, use honest chart scales, and avoid generalizing a constructed sample or treating correlation as causation.

## Conclusion

The script and notebook provide a reproducible path from basic Python through tabular analysis and communication. Validate the data and explain the limits of a result as carefully as reporting the result itself.

## GitHub project information

The project is ready to publish as `Task-1-Data-Science-Fundamentals`. A repository URL is intentionally not included because none has been supplied or published yet.
