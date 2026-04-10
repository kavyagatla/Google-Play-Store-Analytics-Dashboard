# 📊 Google Play Store Analytics Dashboard

## 📌 Project Overview

This project is an interactive data analysis dashboard built using **Streamlit** to analyze the Google Play Store dataset.
It provides insights into app performance, installs, ratings, and estimated revenue using dynamic visualizations.

---

## 🎯 Objectives

* Analyze app trends across different categories
* Estimate revenue based on installs and pricing
* Identify high-performing apps
* Build an interactive dashboard with filters and visual insights

---

## 🛠️ Tools & Technologies Used

* **Python**
* **Pandas** (Data Cleaning & Analysis)
* **Streamlit** (Dashboard Development)
* **Plotly** (Interactive Visualizations)
* **NumPy**

---

## 📂 Dataset

* Google Play Store Apps Dataset
* Contains information such as:

  * App Name
  * Category
  * Rating
  * Reviews
  * Installs
  * Price
  * Content Rating
  * Android Version

---

## 🔄 Data Preprocessing

* Removed null and inconsistent values
* Converted installs to numeric format
* Cleaned price column (removed `$` symbol)
* Handled invalid values using `coerce`
* Created new features:

  * **Installs_Numeric**
  * **Price_Clean**
  * **Revenue (Installs × Price)**

---

## 📊 Dashboard Features

* 📌 Category-wise analysis
* 📌 Rating vs Installs visualization
* 📌 Revenue estimation
* 📌 Interactive filters (Category, Type)
* 📌 Task-based analytics (Task 1–Task 6)
* 📌 Time-based feature (Task 6 visible only between 1PM–2PM)

---

## 📈 Key Insights

* Free apps dominate in terms of installs
* Paid apps contribute significantly to revenue
* Certain categories like **Games** and **Business** have higher engagement
* High-rated apps tend to have more installs

---

## 🚀 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Google-Play-Store-Analytics-Dashboard.git
```

### 2. Navigate to the folder

```bash
cd Google-Play-Store-Analytics-Dashboard
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

👉 https://google-play-store-analytics-dashboard.onren<img width="1918" height="1023" alt="Screenshot 2026-04-10 133908" src="https://github.com/user-attachments/assets/4d99e3f7-a72f-45e5-9e2e-fae24c64a0cc" />
der.com/

---

## 📷 Screenshots
<img width="1918" height="1023" alt="Screenshot 2026-04-10 133908" src="https://github.com/user-attachments/assets/9a57f13a-4eaa-44dd-9c1a-7f9fb1a852eb" />



---

## 📌 Internship Task Implementation

This project is an extension of the training project where additional internship tasks were implemented as dashboard features, ensuring:

* Use of the same dataset
* Enhanced analytics
* Interactive visualizations

---

## 👩‍💻 Author

**Kavya G**

---

## 📧 Contact

For queries or collaboration:
(Add your email if needed)

---
