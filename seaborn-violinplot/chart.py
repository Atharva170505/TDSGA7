import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data for support efficiency
np.random.seed(42)
departments = ['Sales', 'Tech Support', 'HR', 'Finance']
data = {
    'Department': np.repeat(departments, 100),
    'Resolution_Time': np.concatenate([
        np.random.normal(loc=30, scale=5, size=100),   # Sales
        np.random.normal(loc=45, scale=10, size=100),  # Tech Support
        np.random.normal(loc=25, scale=4, size=100),   # HR
        np.random.normal(loc=35, scale=6, size=100)    # Finance
    ])
}

df = pd.DataFrame(data)

# Professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # 8x8 inches, with dpi=64 => 512x512 pixels

# Create violinplot
ax = sns.violinplot(
    x="Department",
    y="Resolution_Time",
    data=df,
    palette="Set2",
    inner="quartile"
)

# Titles and labels
ax.set_title("Support Resolution Time by Department", fontsize=16, weight="bold")
ax.set_xlabel("Department", fontsize=12)
ax.set_ylabel("Resolution Time (minutes)", fontsize=12)

# Save chart as 512x512 PNG
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
