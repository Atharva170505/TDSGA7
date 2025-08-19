# employee_analysis.py
# Author: 24f1001859@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

# -----------------------------
# Step 1: Create Dataset (sample for 100 employees)
# -----------------------------
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,HR,Latin America,91.4,15,3.8
EMP002,Marketing,Africa,64.58,4,4.1
EMP003,Sales,Middle East,92.54,3,3.7
EMP004,R&D,Africa,93.57,1,4.5
EMP005,Operations,Asia Pacific,80.05,4,4.9
EMP006,HR,Europe,77.3,8,4.2
EMP007,IT,North America,89.6,6,4.4
EMP008,Finance,Asia Pacific,72.1,5,3.9
EMP009,Sales,Europe,85.4,7,4.0
EMP010,HR,Asia Pacific,66.9,2,3.5
"""  # you can expand to 100 rows if needed

from io import StringIO
df = pd.read_csv(StringIO(data))

# -----------------------------
# Step 2: Calculate HR count
# -----------------------------
hr_count = (df["department"] == "HR").sum()
print(f"Number of employees in HR Department: {hr_count}")

# -----------------------------
# Step 3: Create Histogram
# -----------------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="department", palette="Set2")
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()

# Save to buffer (for embedding)
buffer = BytesIO()
plt.savefig(buffer, format="png")
buffer.seek(0)
img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
buffer.close()

# -----------------------------
# Step 4: Build HTML Report
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
    <img src="data:image/png;base64,{img_base64}" alt="Histogram" />
</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)

print("✅ Analysis saved to employee_analysis.html")
