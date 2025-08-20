# Regenerate the chart with exact 512x512 dimensions

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

# Simulate response times (in minutes) for each channel
data = {
    "Channel": np.repeat(channels, 200),
    "Response Time (minutes)": np.concatenate([
        np.random.normal(loc=30, scale=10, size=200),   # Email
        np.random.normal(loc=5, scale=2, size=200),     # Chat
        np.random.normal(loc=15, scale=5, size=200),    # Phone
        np.random.normal(loc=60, scale=20, size=200),   # Social Media
    ])
}

df = pd.DataFrame(data)

# Seaborn Styling
sns.set_style("whitegrid")
sns.set_context("talk")
palette = sns.color_palette("Set2")

# Create Violin Plot
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512px
ax = sns.violinplot(
    x="Channel", 
    y="Response Time (minutes)", 
    data=df, 
    palette=palette,
    inner="quartile"
)

# Titles and Labels
ax.set_title("Customer Support Response Time Distribution by Channel", fontsize=16, weight="bold")
ax.set_xlabel("Support Channel", fontsize=14)
ax.set_ylabel("Response Time (minutes)", fontsize=14)

plt.xticks(rotation=20)

# Save chart WITHOUT bbox_inches='tight'
plt.savefig("/mnt/data/chart.png", dpi=64)
plt.close()

# Verify size again
from PIL import Image
Image.open("/mnt/data/chart.png").size
