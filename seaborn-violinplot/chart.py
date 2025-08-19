import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic business data (Support efficiency example)
np.random.seed(42)
departments = ['IT Support', 'Customer Care', 'Tech Support']
efficiency = []

for dept in departments:
    if dept == 'IT Support':
        data = np.random.normal(loc=70, scale=10, size=100)
    elif dept == 'Customer Care':
        data = np.random.normal(loc=60, scale=15, size=100)
    else:
        data = np.random.normal(loc=75, scale=8, size=100)
    efficiency.extend(zip([dept]*100, data))

# Create DataFrame
df = pd.DataFrame(efficiency, columns=['Department', 'Efficiency'])

# Professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create figure with exact 512x512 pixels
plt.figure(figsize=(8, 8), dpi=64)

# Violin plot with proper hue handling
ax = sns.violinplot(
    x="Department",
    y="Efficiency",
    data=df,
    hue="Department",          # Apply palette by hue
    palette="Set2",
    legend=False               # Avoid duplicate legend
)

# Titles and labels
ax.set_title("Support Department Efficiency Distribution", fontsize=16, pad=15)
ax.set_xlabel("Department", fontsize=12)
ax.set_ylabel("Efficiency Score", fontsize=12)

# Save chart exactly 512x512
plt.savefig("chart.png", dpi=64)
plt.close()
