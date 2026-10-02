import json
import docx

nb_content = {
    'cells': [
        {'cell_type': 'markdown', 'metadata': {}, 'source': ['# Task 4: Data Science Tool Mastery Project\n', 'Mastering NumPy, Pandas, Matplotlib, Seaborn, and Scikit-Learn.']},
        {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': ['import numpy as np\n', 'import pandas as pd\n', 'import matplotlib.pyplot as plt\n', 'import seaborn as sns\n', 'from sklearn.model_selection import train_test_split\n', 'from sklearn.preprocessing import StandardScaler\n', 'from sklearn.linear_model import LogisticRegression\n', 'print("All libraries imported successfully!")']},
        {'cell_type': 'markdown', 'metadata': {}, 'source': ['## 1. NumPy Array Operations']},
        {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': ['arr = np.random.randn(100, 4)\n', 'print("Array Shape:", arr.shape)\n', 'print("Mean:", np.mean(arr), "Std Dev:", np.std(arr))']},
        {'cell_type': 'markdown', 'metadata': {}, 'source': ['## 2. Pandas Data Wrangling']},
        {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': ['df = pd.DataFrame(arr, columns=["Feature1", "Feature2", "Feature3", "Target_Raw"])\n', 'df["Target"] = (df["Target_Raw"] > 0).astype(int)\n', 'print(df.head())\n', 'print(df.describe())']},
        {'cell_type': 'markdown', 'metadata': {}, 'source': ['## 3. Data Visualization']},
        {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': ['plt.figure(figsize=(8, 5))\n', 'sns.heatmap(df.corr(), annot=True, cmap="coolwarm")\n', 'plt.title("Feature Correlation Matrix")\n', 'plt.savefig("Task-4-Data-Science-Tool-Mastery/correlation.png")\n', 'plt.close()']},
        {'cell_type': 'markdown', 'metadata': {}, 'source': ['## 4. Scikit-Learn Machine Learning Pipeline']},
        {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': ['X = df[["Feature1", "Feature2", "Feature3"]]\n', 'y = df["Target"]\n', 'X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n', 'scaler = StandardScaler()\n', 'X_train_scaled = scaler.fit_transform(X_train)\n', 'model = LogisticRegression()\n', 'model.fit(X_train_scaled, y_train)\n', 'print("Model Accuracy:", model.score(scaler.transform(X_test), y_test))']}
    ],
    'metadata': {'language_info': {'name': 'python'}},
    'nbformat': 4,
    'nbformat_minor': 2
}

with open('Task-4-Data-Science-Tool-Mastery/Task4_Tool_Mastery.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb_content, f, indent=2)

doc = docx.Document()
doc.add_heading('Task 4: Data Science Tool Mastery Project', level=0)
doc.add_heading('1. Overview & Tool Stack Mastery', level=1)
doc.add_paragraph('This project demonstrates proficiency across industry-standard Python libraries essential for data analytics and data science workflows: NumPy, Pandas, Matplotlib, Seaborn, and Scikit-Learn.')
doc.add_heading('2. Practical Implementation & Workflows', level=1)
doc.add_paragraph('- NumPy: Vectorized array manipulations, random sampling, and array reshaping.')
doc.add_paragraph('- Pandas: DataFrame creation, statistical summarization, feature creation, and filtering.')
doc.add_paragraph('- Matplotlib & Seaborn: Custom plot generation, formatting, and correlation matrix visualizations.')
doc.add_paragraph('- Scikit-Learn: Feature scaling, dataset splitting, and predictive modeling using Logistic Regression.')
doc.add_heading('3. Portfolio Summary', level=1)
doc.add_paragraph('The attached script and Jupyter Notebook validate end-to-end fluency with core Python data science tools.')

output_path = 'Task-4-Data-Science-Tool-Mastery/Task_4_Tool_Mastery_Report.docx'
doc.save(output_path)
print('SUCCESS: Task 4 Notebook and Word Report generated successfully!')
