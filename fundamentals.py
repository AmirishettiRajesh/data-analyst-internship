"""Task 1: Data Science Fundamentals Assessment.

Run from this folder with: python fundamentals.py
The script creates the sample CSV, visualization files, and DOCX report.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt, RGBColor


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "outputs"
CHART_DIR = OUTPUT_DIR / "charts"
CSV_PATH = PROJECT_DIR / "student_performance.csv"
RESULTS_PATH = OUTPUT_DIR / "results.txt"
REPORT_PATH = PROJECT_DIR / "report" / "Task_1_Data_Science_Fundamentals_Report.docx"
RANDOM_SEED = 42

# This fictional, hand-authored dataset contains no real student information.
SAMPLE_RECORDS = [
    (1001, "Avery", 19, "Female", 8.0, 96, 82, 86),
    (1002, "Blake", 20, "Male", 5.5, 88, 74, 76),
    (1003, "Casey", 18, "Female", 3.0, 81, 68, 70),
    (1004, "Devon", 21, "Male", 9.0, 97, 90, 92),
    (1005, "Emery", 19, "Female", 6.5, 91, 78, 81),
    (1006, "Finley", 20, "Male", 2.5, 73, 61, 64),
    (1007, "Gray", 18, "Non-binary", 7.0, 93, 80, 83),
    (1008, "Harper", 22, "Female", 4.0, 85, 70, 72),
    (1009, "Indigo", 19, "Male", 10.0, 99, 94, 96),
    (1010, "Jordan", 20, "Female", 5.0, 87, 73, 75),
    (1011, "Kai", 18, "Male", 6.0, 90, 76, 79),
    (1012, "Logan", 21, "Female", 3.5, 79, 66, 68),
    (1013, "Morgan", 19, "Non-binary", 8.5, 95, 88, 90),
    (1014, "Noah", 20, "Male", 4.5, 84, 72, 74),
    (1015, "Oakley", 18, "Female", 7.5, 92, 84, 87),
    (1016, "Parker", 22, "Male", 1.5, 68, 55, 58),
    (1017, "Quinn", 19, "Female", 6.0, 89, 77, 80),
    (1018, "Riley", 21, "Male", 2.0, 75, 59, 62),
    (1019, "Sage", 18, "Female", 9.5, 98, 92, 94),
    (1020, "Taylor", 20, "Male", 5.0, 86, 71, 75),
]
COLUMNS = ["Student_ID", "Name", "Age", "Gender", "Study_Hours", "Attendance", "Assignments_Score", "Exam_Score"]


def make_sample_data() -> pd.DataFrame:
    """Build the reproducible fictional student-performance dataset."""
    return pd.DataFrame(SAMPLE_RECORDS, columns=COLUMNS)


def validate_data(data: pd.DataFrame) -> None:
    """Fail early when required columns, keys, ranges, or types are invalid."""
    required = set(COLUMNS)
    missing_columns = required.difference(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")
    if data[list(required)].isna().any().any():
        raise ValueError("Required fields must not contain missing values.")
    if data["Student_ID"].duplicated().any():
        raise ValueError("Student_ID values must be unique.")
    for column in ["Age", "Study_Hours", "Attendance", "Assignments_Score", "Exam_Score"]:
        if not pd.api.types.is_numeric_dtype(data[column]):
            raise TypeError(f"{column} must contain numeric values.")
    if not data["Attendance"].between(0, 100).all():
        raise ValueError("Attendance must be between 0 and 100.")
    for column in ["Assignments_Score", "Exam_Score"]:
        if not data[column].between(0, 100).all():
            raise ValueError(f"{column} must be between 0 and 100.")
    if not data["Age"].between(16, 100).all() or not data["Study_Hours"].between(0, 168).all():
        raise ValueError("Age or Study_Hours is outside a plausible range.")


def demonstrate_python_fundamentals() -> dict[str, object]:
    """Exercise core language concepts and return a few useful example values."""
    student_count: int = 20
    example_study_hours: float = 5.8
    assessment_name: str = "Data Science Fundamentals"
    is_reproducible: bool = True
    converted_count = int("20")
    arithmetic_example = 8 + 2 * 3
    comparison_example = student_count >= converted_count
    logical_example = is_reproducible and example_study_hours > 0

    if example_study_hours >= 8:
        study_band = "high"
    elif example_study_hours >= 4:
        study_band = "moderate"
    else:
        study_band = "low"

    study_totals: list[int] = []
    for study_hour in [2, 4, 6]:
        study_totals.append(study_hour * 2)
    countdown: list[int] = []
    counter = 3
    while counter > 0:
        countdown.append(counter)
        counter -= 1

    def calculate_pass_rate(scores: list[int], pass_mark: int = 70) -> float:
        """Return the proportion of scores meeting the pass mark."""
        if not scores:
            return 0.0
        return sum(score >= pass_mark for score in scores) / len(scores)

    example_list = ["clean", "validate", "analyze"]
    example_tuple = ("Age", "int64")
    example_set = {"Python", "NumPy", "Python"}
    example_dictionary = {"dataset": "student performance", "rows": student_count}
    try:
        invalid_number = int("not a number")
    except ValueError:
        invalid_number = None

    # Basic file handling uses a small temporary CSV and always closes it safely.
    temporary_path = OUTPUT_DIR / "file_handling_example.csv"
    try:
        with temporary_path.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["concept", "value"])
            writer.writerow(["assessment", assessment_name])
        with temporary_path.open("r", newline="", encoding="utf-8") as csv_file:
            file_example = next(csv.reader(csv_file))
    finally:
        temporary_path.unlink(missing_ok=True)

    return {
        "study_band": study_band,
        "study_totals": study_totals,
        "countdown": countdown,
        "pass_rate_example": calculate_pass_rate([68, 75, 91]),
        "list_example": example_list,
        "tuple_example": example_tuple,
        "set_example": sorted(example_set),
        "dictionary_example": example_dictionary,
        "exception_example": invalid_number,
        "file_example": file_example,
        "operator_examples": (arithmetic_example, comparison_example, logical_example),
    }


def calculate_statistics(data: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    """Calculate descriptive statistics and score/study-hour correlations."""
    scores = data["Exam_Score"]
    summary = pd.Series({
        "Mean": scores.mean(),
        "Median": scores.median(),
        "Mode": scores.mode().iloc[0],
        "Minimum": scores.min(),
        "Maximum": scores.max(),
        "Range": scores.max() - scores.min(),
        "Variance (sample)": scores.var(ddof=1),
        "Standard deviation (sample)": scores.std(ddof=1),
        "25th percentile": scores.quantile(0.25),
        "75th percentile": scores.quantile(0.75),
    })
    correlations = data[["Study_Hours", "Attendance", "Assignments_Score", "Exam_Score"]].corr()
    return summary, correlations


def demonstrate_numpy(data: pd.DataFrame) -> dict[str, object]:
    """Show array creation, access, arithmetic, reshaping, and reductions."""
    one_dimensional = np.array(data["Exam_Score"].to_numpy())
    two_dimensional = data[["Study_Hours", "Exam_Score"]].to_numpy(dtype=float)
    example_grid = np.arange(1, 7).reshape(2, 3)
    return {
        "one_dimensional": one_dimensional,
        "two_dimensional": two_dimensional,
        "first_score": one_dimensional[0],
        "first_three_scores": one_dimensional[:3],
        "array_addition_example": example_grid + 10,
        "reshaped_example": example_grid,
        "mean": float(np.mean(one_dimensional)),
        "minimum": int(np.min(one_dimensional)),
        "maximum": int(np.max(one_dimensional)),
        "standard_deviation": float(np.std(one_dimensional, ddof=1)),
    }


def demonstrate_data_quality(data: pd.DataFrame) -> dict[str, int]:
    """Create controlled quality issues, detect them, then clean a copy."""
    imperfect_data = data.copy()
    imperfect_data.loc[0, "Attendance"] = np.nan
    imperfect_data = pd.concat([imperfect_data, imperfect_data.iloc[[1]]], ignore_index=True)
    missing_before = int(imperfect_data.isna().sum().sum())
    duplicates_before = int(imperfect_data.duplicated().sum())
    cleaned_data = imperfect_data.drop_duplicates().copy()
    cleaned_data["Attendance"] = cleaned_data["Attendance"].fillna(cleaned_data["Attendance"].median())
    first_quartile = cleaned_data["Exam_Score"].quantile(0.25)
    third_quartile = cleaned_data["Exam_Score"].quantile(0.75)
    interquartile_range = third_quartile - first_quartile
    lower_bound = first_quartile - 1.5 * interquartile_range
    upper_bound = third_quartile + 1.5 * interquartile_range
    outlier_count = int((~cleaned_data["Exam_Score"].between(lower_bound, upper_bound)).sum())
    return {
        "missing_before": missing_before,
        "duplicates_before": duplicates_before,
        "missing_after": int(cleaned_data.isna().sum().sum()),
        "duplicates_after": int(cleaned_data.duplicated().sum()),
        "cleaned_rows": len(cleaned_data),
        "exam_score_outliers": outlier_count,
    }


def create_visualizations(data: pd.DataFrame, correlations: pd.DataFrame) -> list[Path]:
    """Save six legible charts generated directly from the sample dataset."""
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid", palette="colorblind")
    chart_paths: list[Path] = []

    def save_chart(file_name: str) -> None:
        path = CHART_DIR / file_name
        plt.tight_layout()
        plt.savefig(path, dpi=160, bbox_inches="tight")
        plt.close()
        chart_paths.append(path)

    plt.figure(figsize=(7, 4))
    sns.barplot(data=data, x="Gender", y="Exam_Score", errorbar=None)
    plt.title("Mean exam score by gender")
    plt.xlabel("Gender")
    plt.ylabel("Mean exam score (0-100)")
    save_chart("bar_exam_score_by_gender.png")

    plt.figure(figsize=(8, 4))
    sns.lineplot(data=data.sort_values("Study_Hours"), x="Study_Hours", y="Exam_Score", marker="o", errorbar=None)
    plt.title("Exam score by study hours (individual observations)")
    plt.xlabel("Study hours per week")
    plt.ylabel("Exam score (0-100)")
    save_chart("line_exam_score_by_study_hours.png")

    plt.figure(figsize=(7, 4))
    sns.histplot(data=data, x="Exam_Score", bins=8, kde=False)
    plt.title("Distribution of exam scores")
    plt.xlabel("Exam score (0-100)")
    plt.ylabel("Number of students")
    save_chart("histogram_exam_scores.png")

    plt.figure(figsize=(7, 4))
    sns.scatterplot(data=data, x="Study_Hours", y="Exam_Score", hue="Gender", s=70)
    plt.title("Study hours and exam scores")
    plt.xlabel("Study hours per week")
    plt.ylabel("Exam score (0-100)")
    save_chart("scatter_study_hours_exam_score.png")

    plt.figure(figsize=(7, 4))
    sns.boxplot(data=data, x="Gender", y="Exam_Score")
    plt.title("Exam score spread by gender")
    plt.xlabel("Gender")
    plt.ylabel("Exam score (0-100)")
    save_chart("box_exam_scores_by_gender.png")

    plt.figure(figsize=(7, 5))
    sns.heatmap(correlations, annot=True, cmap="vlag", center=0, vmin=-1, vmax=1, fmt=".2f")
    plt.title("Correlation among study and performance measures")
    save_chart("correlation_heatmap.png")
    return chart_paths


def add_report_heading(document: Document, title: str, level: int = 1) -> None:
    heading = document.add_heading(title, level=level)
    heading.paragraph_format.keep_with_next = True


def add_bullet(document: Document, text: str) -> None:
    document.add_paragraph(text, style="List Bullet")


def add_code_block(document: Document, code: str) -> None:
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.left_indent = Inches(0.22)
    paragraph.paragraph_format.space_after = Pt(5)
    run = paragraph.add_run(code)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(35, 62, 79)


def create_report(data: pd.DataFrame, statistics: pd.Series, correlations: pd.DataFrame,
                  quality: dict[str, int], chart_paths: list[Path]) -> None:
    """Generate a formatted report whose numerical content comes from analysis."""
    document = Document()
    section = document.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)
    normal_style = document.styles["Normal"]
    normal_style.font.name = "Calibri"
    normal_style.font.size = Pt(10)
    normal_style.paragraph_format.space_after = Pt(5)
    for style_name, color in [("Heading 1", "174A5B"), ("Heading 2", "26736B")]:
        style = document.styles[style_name]
        style.font.name = "Calibri"
        style.font.color.rgb = RGBColor.from_string(color)

    # Cover page
    title = document.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.paragraph_format.space_before = Inches(1.3)
    title_run = title.add_run("DATA SCIENCE\nFUNDAMENTALS ASSESSMENT")
    title_run.bold = True
    title_run.font.size = Pt(27)
    title_run.font.color.rgb = RGBColor(23, 74, 91)
    subtitle = document.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.add_run("Data Analyst Internship\n\nTask 1:\nData Science Fundamentals Assessment\n\n").bold = True
    subtitle.add_run("Internship duration: 02 October 2026 - 27 November 2026\n")
    subtitle.add_run("Prepared as a beginner-friendly practical assessment\n")
    subtitle.add_run("Dataset: fictional, reproducible student-performance sample")
    document.add_page_break()

    add_report_heading(document, "1. Introduction")
    document.add_paragraph(
        "This report documents a practical introduction to data science using Python. "
        "It progresses from language fundamentals to descriptive statistics, NumPy arrays, "
        "Pandas data preparation, and visual communication. All examples use a small, "
        "fictional student-performance dataset authored for this assignment; no external "
        "dataset or citations are used."
    )
    add_report_heading(document, "2. Objectives")
    for item in [
        "Demonstrate core Python syntax, data types, collections, control flow, functions, exceptions, and file handling.",
        "Calculate descriptive statistics and correlations from actual sample records.",
        "Practice array operations and tabular analysis with NumPy and Pandas.",
        "Create common charts and apply basic validation, cleaning, reproducibility, and privacy principles.",
    ]:
        add_bullet(document, item)
    add_report_heading(document, "3. What is Data Science?")
    document.add_paragraph(
        "Data science combines domain questions, data preparation, computation, and communication. "
        "A responsible workflow clarifies the question, checks the data, chooses suitable analysis, "
        "and reports limitations alongside findings. A descriptive relationship is not proof of causation."
    )
    document.add_paragraph("Workflow used: define fields -> validate records -> summarize -> visualize -> interpret cautiously.")
    add_report_heading(document, "4. Data Science Lifecycle")
    document.add_paragraph(
        "The lifecycle begins by framing a question and identifying appropriate data. It continues through collection, "
        "quality checks, preparation, exploration, analysis, visualization, and communication. In production work, "
        "monitoring and revision follow deployment; this assessment focuses on the preparation-to-communication stages."
    )
    document.add_page_break()

    add_report_heading(document, "5. Python Fundamentals")
    document.add_paragraph(
        "Variables use descriptive names; assignment demonstrates integers, floats, strings, and Booleans. "
        "Arithmetic, comparisons, and logical operators support calculations and conditions. if/elif/else "
        "select a study band; for and while loops iterate; a function encapsulates a reusable pass-rate calculation."
    )
    add_code_block(document, "def calculate_pass_rate(scores, pass_mark=70):\n    if not scores:\n        return 0.0\n    return sum(score >= pass_mark for score in scores) / len(scores)")
    document.add_paragraph(
        "Lists are ordered and mutable; tuples are ordered and immutable; sets retain unique items; "
        "dictionaries map keys to values. A ValueError is caught in a small conversion example. "
        "A context manager writes and reads a short CSV so the file is closed reliably."
    )
    add_report_heading(document, "6. Python Data Types")
    type_table = document.add_table(rows=1, cols=3)
    type_table.style = "Light Shading Accent 1"
    for cell, value in zip(type_table.rows[0].cells, ["Example", "Type", "Use"]):
        cell.text = value
    for row in [
        ("20", "int", "Student count / identifier"),
        ("5.8", "float", "Study hours"),
        ('"Female"', "str", "Category / name"),
        ("True", "bool", "Logical state"),
    ]:
        cells = type_table.add_row().cells
        for cell, value in zip(cells, row):
            cell.text = value
    document.add_paragraph("Explicit conversion (int(\"20\")) is appropriate only when the text represents a valid whole number.")
    add_report_heading(document, "7. Python Data Structures")
    document.add_paragraph("Lists hold ordered mutable values, tuples hold ordered fixed values, sets retain unique values, and dictionaries map keys to values.")
    add_code_block(document, "scores = [68, 75, 91]\ncolumns = ('Age', 'int64')\ntools = {'Python', 'NumPy'}\nstudent = {'Student_ID': 1001, 'Age': 19}")
    add_report_heading(document, "8. Operators")
    document.add_paragraph("Arithmetic operators calculate values; comparison operators evaluate relationships; logical operators combine Boolean conditions.")
    add_code_block(document, "total = 8 + 2 * 3\nmeets_threshold = total >= 10\nvalid = meets_threshold and True")
    add_report_heading(document, "9. Conditional Statements")
    add_code_block(document, "if study_hours >= 8:\n    band = 'high'\nelif study_hours >= 4:\n    band = 'moderate'\nelse:\n    band = 'low'")
    add_report_heading(document, "10. Loops")
    document.add_paragraph("A for loop visits items in a sequence. A while loop repeats while a condition remains true; update its condition each iteration to avoid an infinite loop.")
    add_code_block(document, "for score in [68, 75, 91]:\n    print(score)\n\ncount = 3\nwhile count > 0:\n    count -= 1")
    add_report_heading(document, "11. Functions")
    document.add_paragraph("Functions name a reusable operation, accept inputs, and return a result. The project documents helpers with docstrings and keeps their inputs explicit.")
    add_code_block(document, "def calculate_pass_rate(scores, pass_mark=70):\n    if not scores:\n        return 0.0\n    return sum(score >= pass_mark for score in scores) / len(scores)")
    document.add_page_break()

    add_report_heading(document, "12. Statistical Foundations")
    document.add_paragraph(
        "The following descriptive measures are calculated from all Exam_Score observations. "
        "Variance and standard deviation use the sample convention (ddof=1); percentiles use Pandas' default linear interpolation."
    )
    stats_table = document.add_table(rows=1, cols=2)
    stats_table.style = "Light Shading Accent 1"
    stats_table.rows[0].cells[0].text = "Measure"
    stats_table.rows[0].cells[1].text = "Calculated value"
    for name, value in statistics.items():
        cells = stats_table.add_row().cells
        cells[0].text = name
        cells[1].text = f"{value:.2f}"
    document.add_paragraph(
        f"Pearson correlation between Study_Hours and Exam_Score: "
        f"{correlations.loc['Study_Hours', 'Exam_Score']:.3f}. Correlation describes linear association in this sample, "
        "not a causal effect or a guarantee about other students."
    )
    add_code_block(document, "exam_scores = data['Exam_Score']\nmean_score = exam_scores.mean()\nq3 = exam_scores.quantile(0.75)\ncorrelation = data['Study_Hours'].corr(exam_scores)")
    document.add_page_break()

    add_report_heading(document, "13. NumPy")
    document.add_paragraph(
        "NumPy arrays provide compact numerical structures. The analysis creates a one-dimensional array of exam scores "
        "and a two-dimensional array of study hours and exam scores. It demonstrates indexing, slicing, arithmetic, "
        "reshaping, and mean/minimum/maximum reductions."
    )
    add_code_block(document, "scores = data['Exam_Score'].to_numpy()\nfirst_score = scores[0]\nfirst_three = scores[:3]\nexample = np.arange(1, 7).reshape(2, 3)\nshifted = example + 10")
    document.add_paragraph(
        f"Calculated NumPy score mean: {np.mean(data['Exam_Score'].to_numpy()):.2f}; "
        f"minimum: {np.min(data['Exam_Score'].to_numpy()):.0f}; maximum: {np.max(data['Exam_Score'].to_numpy()):.0f}."
    )
    document.add_paragraph(
        f"NumPy sample standard deviation (ddof=1): {np.std(data['Exam_Score'].to_numpy(), ddof=1):.2f}."
    )
    add_report_heading(document, "14. Pandas")
    document.add_paragraph(
        "A DataFrame is created from records and also exported to CSV, then loaded back for analysis. "
        "head(), shape, info(), and describe() inspect records, dimensions, dtypes, and numeric summaries. "
        "Column selection, threshold filtering, sorting, and groupby summarize the table."
    )
    add_code_block(document, "data = pd.read_csv('student_performance.csv')\nprint(data.head())\nprint(data.shape)\nprint(data.groupby('Gender')['Exam_Score'].mean())")
    grouped = data.groupby("Gender")["Exam_Score"].mean().sort_index()
    document.add_paragraph("Mean exam score by gender in this sample:")
    for group_name, score in grouped.items():
        add_bullet(document, f"{group_name}: {score:.2f}")
    add_report_heading(document, "15. Dataset Description")
    document.add_paragraph(
        f"The CSV contains {len(data)} fictional student records and {data.shape[1]} fields. "
        "Student_ID is a unique identifier; Age is measured in years; Study_Hours is hours per week; "
        "Attendance is a percentage; assignment and exam scores use a 0-100 scale. The records are "
        "synthetic and should not be treated as real student evidence."
    )
    schema_table = document.add_table(rows=1, cols=2)
    schema_table.style = "Light Shading Accent 1"
    schema_table.rows[0].cells[0].text = "Column"
    schema_table.rows[0].cells[1].text = "Meaning"
    for column_name, meaning in [
        ("Student_ID", "Unique fictional identifier"), ("Name", "Fictional first name"),
        ("Age", "Age in years"), ("Gender", "Fictional category"),
        ("Study_Hours", "Study hours per week"), ("Attendance", "Attendance percentage"),
        ("Assignments_Score", "Assignment score out of 100"), ("Exam_Score", "Exam score out of 100"),
    ]:
        cells = schema_table.add_row().cells
        cells[0].text = column_name
        cells[1].text = meaning
    document.add_page_break()

    add_report_heading(document, "16. Data Cleaning")
    document.add_paragraph(
        "The published sample is complete and unique. To demonstrate cleaning without silently altering it, a separate copy "
        "is deliberately given one missing attendance value and one duplicate record. The example counts these issues, "
        "removes the duplicate, and fills missing attendance with the observed median."
    )
    add_code_block(document, "cleaned = imperfect.drop_duplicates().copy()\ncleaned['Attendance'] = cleaned['Attendance'].fillna(cleaned['Attendance'].median())")
    for item in [
        f"Controlled cleaning check: {quality['missing_before']} missing value(s) and {quality['duplicates_before']} duplicate row(s) before cleaning; "
        f"{quality['missing_after']} missing and {quality['duplicates_after']} duplicate rows after.",
        "Validate required columns, unique identifiers, numeric dtypes, and plausible score/attendance ranges before analysis.",
        "Keep meaningful variable names, comments for intent, and docstrings for reusable functions.",
        "Use a fixed seed when randomness is introduced; retain the sample data and explicit package requirements.",
        "Do not expose identifiable student records; this exercise uses fictional names and IDs only.",
        "Avoid truncated axes and unsupported causal claims; report sample size, units, and limitations.",
    ]:
        add_bullet(document, item)
    document.add_page_break()

    add_report_heading(document, "17. Data Visualization")
    document.add_paragraph(
        "Matplotlib and Seaborn generate a bar chart, line chart, histogram, scatter plot, box plot, and correlation heatmap. "
        "Axes name the measures and include units. The line chart connects individual observations ordered by study hours; "
        "it is descriptive, not a time-series trend. The heatmap scale is fixed from -1 to 1."
    )
    for chart_path in chart_paths[:3]:
        document.add_picture(str(chart_path), width=Inches(5.5))
        document.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_page_break()
    for chart_path in chart_paths[3:]:
        document.add_picture(str(chart_path), width=Inches(5.1))
        document.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.add_page_break()

    add_report_heading(document, "18. Results and Observations")
    document.add_paragraph(
        f"The dataset has {len(data)} students and {data.shape[1]} fields. Exam scores range from "
        f"{statistics['Minimum']:.0f} to {statistics['Maximum']:.0f}, with mean {statistics['Mean']:.2f} and median {statistics['Median']:.2f}. "
        f"The observed Study_Hours/Exam_Score correlation is {correlations.loc['Study_Hours', 'Exam_Score']:.3f}."
    )
    document.add_paragraph(
        "These are descriptive results from a small, deliberately constructed teaching sample. They should not be generalized "
        "to an actual school population. Differences across groups may reflect the hand-authored records and do not establish causes."
    )
    add_report_heading(document, "19. Data Science Best Practices")
    for item in [
        "Reproducibility: keep source data and package requirements explicit; fix random seeds where randomness is used.",
        "Readable code: use meaningful names, focused functions, comments for non-obvious logic, and documentation.",
        "Data quality: validate schemas, types, valid ranges, nulls, duplicates, and potential outliers before analysis.",
        "Privacy: use synthetic or de-identified data and avoid sharing student-level records without authorization.",
        "Visualization: label units, use honest scales, and make plots answer a clear question.",
        "Interpretation: report sample scope and uncertainty; association alone does not support causal claims.",
    ]:
        add_bullet(document, item)
    add_report_heading(document, "20. Challenges")
    document.add_paragraph(
        "A small sample limits statistical generalization. Sample variance differs from population variance, so ddof=1 is stated explicitly. "
        "Missing-value strategies depend on context; median imputation here is solely an introductory demonstration. "
        "A correlation heatmap is descriptive and can obscure small-sample uncertainty."
    )
    add_report_heading(document, "21. Conclusion")
    document.add_paragraph(
        "This assessment connects Python fundamentals with a reproducible data-analysis workflow. The script, notebook, "
        "generated CSV, figures, and report provide a practical reference for basic cleaning, statistics, and visualization. "
        "The most important takeaway is to validate data and communicate the scope and limitations of results alongside the numbers."
    )
    add_report_heading(document, "22. Technologies Used")
    document.add_paragraph("Python 3.11; NumPy; Pandas; Matplotlib; Seaborn; Jupyter Notebook; python-docx.")
    add_report_heading(document, "23. Project Structure")
    add_code_block(document, "Task-1-Data-Science-Fundamentals/\n  fundamentals.py\n  fundamentals.ipynb\n  student_performance.csv\n  requirements.txt\n  README.md\n  report/Task_1_Data_Science_Fundamentals_Report.docx\n  outputs/charts/\n  outputs/results.txt")
    add_report_heading(document, "24. GitHub Repository Placeholder")
    document.add_paragraph(
        "GitHub repository URL: [Add the repository URL after publishing]. This placeholder is intentionally left for the intern to complete; no repository is claimed to exist."
    )
    document.add_paragraph("Internship task: Data Science Fundamentals Assessment | Duration: 02-Oct-2026 to 27-Nov-2026.")

    # Simple consistent footer with page number field.
    for report_section in document.sections:
        footer = report_section.footer.paragraphs[0]
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        footer.add_run("Data Science Fundamentals Assessment | Task 1")
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    document.save(REPORT_PATH)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    if not CSV_PATH.exists():
        make_sample_data().to_csv(CSV_PATH, index=False)
    loaded_data = pd.read_csv(CSV_PATH)
    validate_data(loaded_data)

    python_examples = demonstrate_python_fundamentals()
    statistics, correlations = calculate_statistics(loaded_data)
    numpy_examples = demonstrate_numpy(loaded_data)
    quality = demonstrate_data_quality(loaded_data)
    charts = create_visualizations(loaded_data, correlations)
    create_report(loaded_data, statistics, correlations, quality, charts)

    grouped = loaded_data.groupby("Gender").agg(
        Student_Count=("Student_ID", "count"),
        Mean_Exam_Score=("Exam_Score", "mean"),
        Median_Exam_Score=("Exam_Score", "median"),
    )
    results = [
        "DATA SCIENCE FUNDAMENTALS ASSESSMENT - RESULTS",
        f"Dataset: {CSV_PATH.name} ({loaded_data.shape[0]} records, {loaded_data.shape[1]} columns)",
        "All records are fictional and created for this learning exercise.",
        "",
        "Exam_Score descriptive statistics:",
        statistics.round(2).to_string(),
        "",
        "Exam score aggregation by Gender:",
        grouped.round(2).to_string(),
        "",
        f"Study_Hours / Exam_Score Pearson correlation: {correlations.loc['Study_Hours', 'Exam_Score']:.3f}",
        f"NumPy score mean/min/max/sample standard deviation: {numpy_examples['mean']:.2f} / "
        f"{numpy_examples['minimum']} / {numpy_examples['maximum']} / {numpy_examples['standard_deviation']:.2f}",
        f"Controlled cleaning (missing before/after): {quality['missing_before']}/{quality['missing_after']}",
        f"Controlled cleaning (duplicates before/after): {quality['duplicates_before']}/{quality['duplicates_after']}",
        f"Exam score outliers by the 1.5*IQR rule: {quality['exam_score_outliers']}",
        "",
        "Interpretation: descriptive statistics and correlations describe this constructed sample only; they do not prove causation.",
        f"Charts saved: {len(charts)} in {CHART_DIR.relative_to(PROJECT_DIR)}",
        f"Report saved: {REPORT_PATH.relative_to(PROJECT_DIR)}",
    ]
    RESULTS_PATH.write_text("\n".join(results) + "\n", encoding="utf-8")
    print("\n".join(results))


if __name__ == "__main__":
    main()
