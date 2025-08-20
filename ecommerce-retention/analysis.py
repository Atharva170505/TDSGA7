# analysis.py
# Email for verification: 24f1001859@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

INDUSTRY_TARGET = 85.0

def main():
    df = pd.read_csv("data.csv")
    # Compute average retention rate
    avg = round(df["retention_rate"].mean(), 1)
    print(f"Average customer retention rate (2024): {avg}")
    assert avg == 72.6, "Average should be 72.6 as specified in the brief."

    # Line chart with target benchmark
    plt.figure(figsize=(8, 6))
    plt.plot(df["quarter"], df["retention_rate"], marker="o")
    plt.axhline(INDUSTRY_TARGET, linestyle="--")
    plt.title("Customer Retention Rate by Quarter (2024)")
    plt.xlabel("Quarter")
    plt.ylabel("Retention Rate")
    for x, y in zip(df["quarter"], df["retention_rate"]):
        plt.text(x, y, f"{y}", ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.savefig("figures/retention_trend.png", dpi=150)
    plt.close()

    # Gap vs target by quarter (bar)
    gaps = INDUSTRY_TARGET - df["retention_rate"]
    plt.figure(figsize=(8, 6))
    plt.bar(df["quarter"], gaps)
    plt.title("Gap to Industry Target (85) by Quarter")
    plt.xlabel("Quarter")
    plt.ylabel("Gap (Target - Actual)")
    for x, g in zip(df["quarter"], gaps):
        plt.text(x, g, f"{g:.2f}", ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.savefig("figures/gap_by_quarter.png", dpi=150)
    plt.close()

if __name__ == "__main__":
    main()
