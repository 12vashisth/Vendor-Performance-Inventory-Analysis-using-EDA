Vendor Performance & Inventory Analysis using EDA
📌 Overview

This project performs Exploratory Data Analysis (EDA) on vendor sales and procurement data to extract meaningful business insights. The goal is to analyze vendor performance, pricing strategies, and inventory efficiency to support data-driven decision-making.

🎯 Objectives
Evaluate vendor performance based on sales and purchase data
Identify top vendors and brands contributing to revenue
Analyze pricing trends and bulk purchasing impact
Detect inventory inefficiencies and slow-moving stock
Provide insights for cost optimization and profitability
📂 Project Structure
vendor-performance-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_analysis.ipynb
│
├── src/
│   ├── data_cleaning.py
│   └── analysis.py
│
├── visuals/
│
├── reports/
│   └── final_report.md
│
├── requirements.txt
├── README.md
└── .gitignore
📊 Dataset Description

The dataset includes:

Vendor and brand details
Sales and purchase quantities
Pricing and cost information
Inventory-related attributes

Data was cleaned and preprocessed to ensure consistency and accuracy before analysis.

🔍 Key Business Questions
Which vendors contribute most to sales and procurement?
Does bulk purchasing reduce unit cost?
Which vendors have low inventory turnover?
How much capital is tied in unsold inventory?
What are the profit margin trends across vendors?
📈 Analysis Performed
Univariate Analysis – Understanding individual variables
Bivariate Analysis – Exploring relationships between variables
Multivariate Analysis – Combined insights across features
Data Cleaning & Preprocessing
Data Visualization for trend identification
📌 Key Insights
Bulk purchasing significantly reduces unit cost
Large orders show noticeable price advantages
Some vendors maintain high margins with lower sales volume
Certain vendors have low inventory turnover, indicating inefficiency
Inventory analysis reveals capital locked in unsold stock
🛠️ Tools & Technologies
Python
Pandas, NumPy
Matplotlib, Seaborn
Jupyter Notebook
🚀 How to Run
Clone the repository
Navigate to the project folder

Install dependencies:

pip install -r requirements.txt
Open Jupyter Notebook and run the files in notebooks/
📌 Conclusion

This project highlights how EDA can transform raw data into actionable insights. The findings can help businesses improve vendor selection, optimize pricing strategies, and manage inventory more effectively.

🔮 Future Scope
Build predictive models for demand forecasting
Create interactive dashboards using Power BI/Tableau
Apply machine learning techniques for deeper insights
Automate data pipelines for real-time analysis
