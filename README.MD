# 🚖 Uber Supply-Demand Gap Analysis

This is an end-to-end Exploratory Data Analysis (EDA) project that investigates Uber's ride request data to understand the **supply-demand gap**, especially in terms of cancellations, “No Cars Available” responses, and peak-time inefficiencies.

---

## 🎯 Objective

To analyze Uber request patterns from both City and Airport pickup points and uncover:

- When and where the demand exceeds supply
- Which time slots are most problematic
- How to improve service reliability using data-driven insights

---

## 🔧 Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python (Pandas, Seaborn, Matplotlib)** | Data Cleaning & Visualizations |
| **Oracle SQL Developer** | Business Query Insights |
| **Excel** | Interactive Dashboard & KPIs |
| **Git & GitHub** | Version Control & Publishing |

---

## 📁 Folder Structure

| File / Folder                             | Description |
|------------------------------------------|-------------|
| `Uber Request Data.csv`                  | Raw dataset from Uber |
| `Uber_Cleaned_Data - Raw Data.csv`       | Cleaned data used across tools |
| `Uber_Cleaned_Data_Dashboard.xlsx`       | Final Excel dashboard with slicers, KPIs |
| `Uber Supply Demand Gap Insights.py`     | Full Python analysis script |
| `Uber_EDA_Submission_Filled.ipynb`       | Presentation-style notebook version |
| `SQL/`                                   | Folder with SQL screenshots |
| `Uber Supply Demand Gap Insights.sql`    | All 10 SQL queries (insight-based) |
| `README.md`                              | This file |

---

## 📊 Python EDA (VS Code / Jupyter)

- Cleaned & transformed data using `pandas`
- Visualized request patterns:
  - Status vs Time Slot
  - Pickup Point Trends
  - Hourly Heatmap of demand
- Created `Time slot`, `Request hour`, `Request day` features

📁 Notebook: `Uber_EDA_Submission_Filled.ipynb`  
📄 Output: `Uber_Cleaned_Data.xlsx`

---

## 📈 Excel Dashboard Highlights

- KPIs: Total Requests, Completion %, No Cars %, Cancelled %
- Pivot Tables for Status vs Time Slot & Pickup Point
- Line Chart: Hourly request trend
- Slicers: Interactive filtering by slot, point, and status

📄 File: `Uber_Cleaned_Data_Dashboard.xlsx`

---

## 🧾 SQL Insights (Oracle)

Queried cleaned dataset using Oracle SQL Developer:
- Status distribution
- Demand by hour & pickup point
- Peak failure times
- Completion rate trends

📄 File: `Uber Supply Demand Gap Insights.sql`  
📷 Screenshots in: `SQL/`

---

## 💡 Key Insights (Cross-Tool Summary)

- ❌ **Morning (5–10 AM)** & **Late Night (0–5 AM)** show high cancellations and “No Cars Available”
- 🛫 **Airport pickups** face more failures than City pickups
- 🔁 Completion rate is ~41% (very low!)
- 📈 Peak demand: 5 AM to 10 AM
- ⚠️ "No Cars Available" dominates failure reasons during peak time

---

## 📌 Recommendations

- Reallocate driver supply during peak time slots
- Increase real-time tracking of service failures via dashboards
- Prioritize service at Airport during early morning slots
- Use SQL automation to track demand weekly

---

## 🗂️ How to Run

| Task         | How to Run |
|--------------|------------|
| 🐍 Python     | Open `.ipynb` or `.py` file in VS Code / Jupyter |
| 📊 Excel      | Open `Uber_Cleaned_Data_Dashboard.xlsx` |
| 🧠 SQL        | Use Oracle SQL Developer, import cleaned `.csv`, run `.sql` |

---

## 📸 Dashboard Preview

Dashboard Preview](Screenshot 2025-06-19 140908.png)


---

## 🧑‍💻 Author

**Ronak Patel**  
[GitHub Profile](https://github.com/ronak171990)

---

## 🌐 Live Project Link

🔗 [Uber Supply-Demand Gap GitHub Repo](https://github.com/ronak171990/Uber-Supply-Demand-Gap)
