

# 🎓 BEYOND THE GRADES: Analysis of Student Mental Well-Being

This repository presents a comprehensive data-driven analysis exploring the impact of academic and lifestyle stress on student mental health. The study investigates how factors like sleep duration, dietary habits, financial pressure, academic workload, and study satisfaction influence the psychological well-being of students—highlighting their direct relationship with depression and suicidal thoughts.

Using real-world survey data and interactive visualizations, the project reveals patterns that can help educators, institutions, and policymakers better understand the hidden burdens students carry beyond academic performance.

---

## 📌 Objectives

- Analyze demographic, behavioral, and academic factors that influence student mental health.
- Understand the correlation between academic pressure, financial stress, and depression.
- Examine how study satisfaction and sleep habits impact mental wellness.
- Use visual analytics to identify trends and draw meaningful, evidence-based conclusions.

---

## 📊 Analyses Performed

### 📌 1. **Demographic Analysis**
- **Gender Distribution**: Bar chart and count analysis
- **Age Categories**: Pie chart distribution of age groups
- **Family History of Mental Illness**: Assessed for correlation with depression

### 📌 2. **Behavioral & Lifestyle Analysis**
- **Dietary Habits**: Pie chart & bar chart to explore their effect on depression
- **Sleep Duration**: Linked with both depression and suicidal thoughts (box plots, bar charts)
- **Study Satisfaction**: Correlated with both depression and study hours
- **Study Hours**: Analyzed against both study satisfaction and depressive symptoms

### 📌 3. **Mental Health Indicators**
- **Depression (Yes/No)**: Binary distribution analysis
- **Suicidal Thoughts**: Evaluated by frequency and in relation to sleep habits
- **Financial Stress**: Visualized to see how strongly it relates to depression
- **Academic Pressure**: Analyzed across depression and study behavior

### 📌 4. **Advanced Visual Analytics**
- **Correlation Heatmap**: Shows relationships between behavioral variables and depression
- **3D Scatter Plot**: Visualizes interactions between study hours, academic pressure, and study satisfaction
- **Ternary Plot**: Analyzes the balance between study time, stress, and pressure
- **Heatmaps**: Show combined effects of sleep, suicidal thoughts, and academic load

---

## 📈 Key Insights & Findings

- Students experiencing **high academic pressure and financial stress** are significantly more prone to depression.
- **Sleep deprivation** (especially < 6 hours) is associated with higher suicidal ideation and depressive symptoms.
- Students reporting **low study satisfaction** despite long study hours showed higher mental distress.
- **Unhealthy dietary habits** are more common among students suffering from depression.
- A **strong correlation** was observed between mental health issues and lifestyle behaviors, suggesting the need for holistic interventions.

---

## ✅ Conclusion

This analysis demonstrates that student mental health is deeply intertwined with their academic and lifestyle conditions. Depression and psychological distress are not isolated issues but are often the result of chronic academic overload, lack of rest, unhealthy habits, and emotional pressure. Educational institutions must recognize these interconnected factors and prioritize student well-being alongside academic performance by promoting mental health awareness, offering counseling resources, and fostering healthier routines.

---

## 📁 Project Structure

| File Name                            | Description                                           |
|-------------------------------------|-------------------------------------------------------|
| `BEYOND_THE_GRADES_ANALYSIS_OF_STUDENT_MENTAL_WELL_BEING.ipynb` | Full Google Colab notebook with code and visualizations |
| `Depression Student Dataset.csv`    | Cleaned dataset used for all analyses                 |
| `app.py` (optional)                 | Dash dashboard script with 22 interactive visualizations |
| `README.md`                         | This project summary and documentation                |

---

## 🛠️ Technologies Used

- **Python** – Core programming language
- **Pandas** – Data manipulation
- **Seaborn & Matplotlib** – Statistical visualization
- **Plotly Express** – Interactive charts
- **Dash** – Web-based interactive dashboard
- **Google Colab** – Development environment

---

## 🚀 Interactive Dashboard

This project includes an `Dash`-based dashboard with 22 interactive visualizations to explore patterns in depression, suicidal thoughts, academic workload, and behavior.

> To launch the dashboard locally:
```bash
python app.py
