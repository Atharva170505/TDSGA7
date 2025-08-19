# employee_analysis.py
# Author: 24f1001859@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Step 1: Create Sample Dataset
# -----------------------------
data = {
    "EmployeeID": range(1, 101),
    "Department": [
        "HR", "Finance", "IT", "Sales", "Marketing"
    ] * 20,  # repeating to make 100 employees
    "Region": [
        "North", "South", "East", "West", "Central"
    ] * 20,
    "PerformanceScore": [70, 85, 90, 60, 75] * 20
}

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Calculate Frequency Count for HR
# -----------------------------
hr_count = (df["Department"] == "HR").sum()
print(f"Number of employees in HR Department: {hr_count}")

# -----------------------------
# Step 3: Create Histogram
# -----------------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Department", palette="Set2")
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()

# Save histogram as PNG
plt.savefig("department_histogram.png")

# -----------------------------
# Step 4: Save as HTML Report
# -----------------------------
html_content = f"""
<html>
<head>
    <title>Employee Performance Analysis</title>
</head>
<body>
    <h1>Employee Performance Analysis</h1>
    <p><b>Email:</b> 24f1001859@ds.study.iitm.ac.in</p>
    <p><b>Number of employees in HR Department:</b> {hr_count}</p>
    <h2>Department Distribution Histogram</h2>
    <img src="department_histogram.png" alt="Histogram">
</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)

print("Analysis saved to employee_analysis.html")
