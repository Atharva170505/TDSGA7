# analysis.py
# Author: Atharva Thakre
# Email: 24f1001859@ds.study.iitm.ac.in
# Purpose: Interactive data analysis with Marimo

import marimo as mo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Cell 1: Generate dataset
# -------------------------------
# This cell creates synthetic data with a known relationship.
# Other cells will depend on `df`.

x = np.linspace(0, 10, 200)
y = 3 * x + np.random.normal(0, 3, 200)
df = pd.DataFrame({"x": x, "y": y})

mo.md("### Dataset generated with linear trend and noise.")

# -------------------------------
# Cell 2: Slider for sampling
# -------------------------------
# This slider controls how many points from df we sample.
# Downstream cells will update automatically.

sample_size = mo.ui.slider(10, 200, value=50)

mo.md(f"#### Current Sample Size: **{sample_size}**")

# -------------------------------
# Cell 3: Dependent variable sampling
# -------------------------------
# Uses `sample_size` from previous cell to sample data from df.

sample_df = df.sample(sample_size.value)

mo.md(f"Sampling **{sample_size.value}** points from dataset.")

# -------------------------------
# Cell 4: Visualization
# -------------------------------
# Depends on sample_df -> re-renders automatically when slider changes.

fig, ax = plt.subplots()
ax.scatter(sample_df["x"], sample_df["y"], color="blue", alpha=0.6, label="Sampled Data")
ax.set_title(f"Scatter Plot of Sampled Data ({sample_size.value} points)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

fig
