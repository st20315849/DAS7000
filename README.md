# Air Quality Index (AQI) Prediction System 🌍🌬️

This project provides an end-to-end data science solution for monitoring and predicting the Air Quality Index (AQI) across 26 major Indian cities. It includes a merged dataset from multiple sources, comprehensive Exploratory Data Analysis (EDA), and a Random Forest machine learning model deployed via a Streamlit GUI.

## 🚀 Project Overview

Air pollution is a significant health hazard in urban India. This project aims to:

1. Consolidate air quality data from 26 cities (2015–2020).
2. Analyze the impact of various pollutants like PM2.5, PM10, and NO2.
3. Predict AQI levels using a trained Random Forest Regressor.
4. Deploy an interactive dashboard for public use.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Data Handling:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (Random Forest Regressor)
- **Visualization:** Matplotlib, Seaborn
- **Web App/GUI:** Streamlit

## 📁 File Structure

| File | Description |
|------|-------------|
| `merged_air_quality_data.csv` | The final master dataset (29,531 rows) |
| `analysis_script.py` | Python code for merging data and generating EDA visualizations |
| `app.py` | The Streamlit application script |
| `model.pkl` | The trained Random Forest model |
| `imputer.pkl` | The median imputer used for handling missing pollutant data |

## 📊 Key Findings from EDA

- **Dominant Pollutants:** PM2.5 and PM10 show a strong linear correlation with AQI (r ≈ 0.85).
- **Trends:** Pollution levels peak significantly during winter months (October–February), particularly in northern cities like Delhi.
- **Model Accuracy:** The Random Forest model achieved an R² score of 0.89, making it highly reliable for short-term prediction.

## 💻 How to Run

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/AQI-Prediction-System.git
   ```

2. **Install Dependencies:**
   ```bash
   pip install pandas scikit-learn streamlit matplotlib seaborn
   ```

3. **Launch the App:**
   ```bash
   streamlit run app.py
   ```

## 📝 References

- Lim, C.H., et al. (2020). *Air pollution and its health impacts in Indian cities.*
- Brauer, M., et al. (2016). *Exposure-Response Relationships for Health Effects of Air Pollution.*
