# Supply Chain Correlation Analysis

This project analyzes relationships between key supply chain performance metrics using Excel’s **Data Analysis ToolPak** and **Conditional Formatting**.  
The correlation matrix and heatmap provide clear insights for business decision-making and executive reporting.

## Files
- `correlation.csv` — Correlation matrix values exported from Excel
- `heatmap.png` — Heatmap visualization of correlation values (512x512 px)
- `README.md` — Project documentation

## Business Insights
- **Supplier Lead Time** and **Cost Per Unit** are highly positively correlated (**0.96**).
- **Order Frequency** is strongly negatively correlated with both **Supplier Lead Time** (**-0.90**) and **Cost Per Unit** (**-0.87**).
- **Delivery Performance** is negatively correlated with **Supplier Lead Time** (**-0.93**) and **Cost Per Unit** (**-0.91**).
- These insights suggest that **shortening supplier lead time** may improve delivery performance and reduce costs.

## Methodology
1. Enabled the **Analysis ToolPak** in Excel.
2. Generated a correlation matrix:  
   *Data → Data Analysis → Correlation → Select data range with labels → Output new worksheet.*
3. Exported the correlation matrix as `correlation.csv`.
4. Applied Excel conditional formatting:  
   *Home → Conditional Formatting → Color Scales → Red–White–Green (Red = low, White = neutral, Green = high).*
5. Took a screenshot and resized it to 512×512 px (`heatmap.png`).

## Contact
Email: 24f1001859@ds.study.iitm.ac.in
