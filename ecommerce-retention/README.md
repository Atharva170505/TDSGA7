# E-commerce Customer Retention Analysis (2024)

**Email (verification): 24f1001859@ds.study.iitm.ac.in**

This pull request analyzes quarterly customer retention performance versus the **industry target of 85** and provides an executive-ready data story with actions to close the gap.

## Dataset

| Quarter | Retention Rate |
|--------:|----------------:|
| Q1      | 65.5            |
| Q2      | 74.53           |
| Q3      | 72.31           |
| Q4      | 78.05           |

**Average (2024): 72.6**

> Benchmark target: **85**

## How to run

```bash
python analysis.py
```

This will:
- Compute and print the average (expected **72.6**).
- Generate charts in `figures/`:
  - `retention_trend.png`
  - `gap_by_quarter.png`

## Visualizations

- **Trend vs Target**: `figures/retention_trend.png`  
- **Gap by Quarter**: `figures/gap_by_quarter.png`

## Key Findings

1. **Underperformance vs Target**: The annual average retention is **72.6**, which is **12.4 points below** the industry target of **85** (a shortfall of ~14.6%).  
2. **Positive momentum in H2**: Retention improves from **65.5 (Q1)** to **78.05 (Q4)**, narrowing the gap from **-19.5** to **-6.95** points.  
3. **Volatility mid-year**: Q3 dips to **72.31**, interrupting the Q2 momentum and signaling sensitivity to seasonal or operational factors.

## Business Implications

- **Revenue at risk**: Lower retention raises acquisition costs and reduces LTV, pressuring marketing and margin targets.  
- **Cohort leakage**: The Q3 softness suggests churn drivers in specific segments (e.g., first-repeat window, delivery SLAs, returns friction).  
- **Operational coordination**: Improvements in Q4 indicate that targeted changes (promotions, support SLAs, returns policy) correlate with better retention.

## Recommendations to Reach Target 85

**Solution: implement targeted retention campaigns.**

1. **Cohort-specific lifecycle journeys**:  
   - Identify at-risk cohorts (1st–2nd order, high returners, long delivery zones) and trigger **personalized win-back** flows (email/SMS/in-app).  
2. **Value reinforcement & loyalty**:  
   - Launch tiered **loyalty program** incentives (cashback, expedited shipping, early access). Tie perks to 2nd/3rd purchase milestones.  
3. **Post-purchase experience**:  
   - Tighten **delivery SLAs**, clarify **returns** and reduce refund friction; proactive WISMO alerts.  
4. **Offer optimization**:  
   - Use **uplift modeling** / A/B tests to optimize coupon values and targeting frequency.  
5. **Churn telemetry**:  
   - Define a **retention KPI dashboard** with cohort views and alerting (week-over-week churn spikes).

---

_This PR contains the analysis code, figures, and the data story. It is designed for quick review and decision-making by the executive team._
