# Vendor Performance & Inventory Analysis

## Overview

This project analyzes vendor sales, procurement, and inventory data using Python-based Exploratory Data Analysis (EDA). The objective was to evaluate vendor performance, identify pricing patterns, and uncover inventory inefficiencies that could impact operational costs and profitability.

The analysis focuses on understanding purchasing behavior, inventory turnover, and vendor contribution trends to support better procurement and inventory management decisions.

---

## Business Problem

Businesses often face challenges such as:

* high procurement costs
* inconsistent vendor performance
* excess inventory
* slow-moving stock

This project explores how data analysis can help identify cost-saving opportunities, improve purchasing decisions, and optimize inventory management.

---

## Objectives

* Evaluate vendor performance using sales and purchase data
* Analyze vendor contribution to procurement and revenue
* Compare bulk purchasing and unit purchasing costs
* Identify slow-moving inventory and inventory inefficiencies
* Examine pricing and profit margin trends
* Generate actionable business insights from operational data

---

## Project Structure

```text id="jpkf3w"
vendor-performance-analysis/
│
├── data/
│   ├── begin_inventory.csv
│   ├── end_inventory.csv
│   ├── purchase_prices.csv
│   └── vendor_invoice.csv
│
├── notebooks/
│   ├── inventory_data_cleaning.ipynb
│   └── vendor_performance_analysis.ipynb
│
├── scripts/
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── visuals/
│   ├── vendor_contribution_analysis.png
│   └── profit_margin_analysis.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dataset Information

The dataset contains:

* vendor and supplier details
* inventory records
* purchase transactions
* pricing and cost information
* sales-related metrics

Data cleaning and preprocessing were performed to handle missing values, improve consistency, and prepare the data for analysis.

---

## Key Business Questions

* Which vendors contribute the most to procurement and sales?
* Does bulk purchasing significantly reduce unit cost?
* Which vendors show low inventory turnover?
* How much capital is tied up in unsold inventory?
* What are the profit margin trends across vendors?

---

## Analysis Performed

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Vendor pricing comparison
* Inventory turnover analysis
* Bulk vs. unit purchasing analysis
* Profit margin evaluation
* Statistical comparison of vendor performance
* Data visualization for trend identification

---

## Key Insights

* Bulk purchasing showed noticeable cost advantages in several product categories.
* Large purchase quantities were associated with lower per-unit procurement costs.
* Certain vendors maintained higher profit margins despite lower sales contribution.
* Some inventory categories showed slow turnover, indicating potential overstocking.
* Inventory analysis highlighted capital tied up in unsold stock.

---

## Sample Visualizations

### Vendor Purchase Contribution Analysis

This visualization shows the percentage contribution of top vendors to total procurement volume, highlighting vendor concentration patterns.

![Vendor Contribution Analysis](visuals/vendor_contribution_analysis.png)

---

### Profit Margin Distribution Analysis

Comparison of profit margin distributions between top-performing and low-performing vendors using confidence interval analysis.

![Profit Margin Analysis](visuals/profit_margin_analysis.png)

---

## Business Recommendations

* Increase bulk purchasing for products with stable demand patterns.
* Monitor slow-moving inventory regularly to reduce holding costs.
* Review vendors with high procurement cost but lower profitability contribution.
* Improve inventory tracking to optimize stock levels and purchasing decisions.

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## How to Run

1. Clone the repository
2. Install dependencies:

```bash id="g3h5we"
pip install -r requirements.txt
```

3. Open the notebooks inside the `notebooks/` folder and run the analysis.

---

## Conclusion

This project demonstrates how exploratory data analysis can be used to evaluate vendor performance, identify inventory inefficiencies, and support data-driven procurement decisions. The findings provide practical insights that can help improve operational efficiency and cost management.

---

## Future Improvements

* Build interactive dashboards using Power BI
* Develop predictive models for demand forecasting
* Automate data pipelines for recurring analysis
* Expand analysis with additional operational metrics

