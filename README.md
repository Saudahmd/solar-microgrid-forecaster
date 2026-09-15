# ☀️ Solar Power Generation Forecasting

### Intelligent Multi-Step Forecasting System for Solar Microgrids

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Latest-orange)](https://xgboost.readthedocs.io/)
[![LightGBM](https://img.shields.io/badge/LightGBM-Latest-green)](https://lightgbm.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A complete end-to-end machine learning pipeline for forecasting solar power generation using real-world plant data. The project includes data preprocessing, advanced feature engineering, model comparison, realistic one-step forecasting, and multi-step forecasting.

---

## 📌 Project Highlights

- Real solar power plant data (15-minute resolution)
- Advanced feature engineering (lag features + time-based features)
- Multiple models compared (Linear Regression, Random Forest, LightGBM, XGBoost)
- **Realistic forecasting** (without using current irradiation)
- Multi-step forecasting (next 15–60 minutes)
- Detailed residual & error analysis
- Production-ready model saving

---

## 📊 Dataset

**Source:** [Solar Power Generation Data](https://www.kaggle.com/datasets/anikannal/solar-power-generation-data)

| File | Description |
|------|-------------|
| `Plant_1_Generation_Data.csv` | Power generation data from multiple inverters |
| `Plant_1_Weather_Sensor_Data.csv` | Weather sensor data (Temperature + Irradiation) |

**Duration:** 15 May 2020 – 17 June 2020  
**Resolution:** 15 minutes  
**Final Records after processing:** 3,155

### Features Used

| Feature | Description |
|---------|-------------|
| `IRRADIATION` | Solar irradiance |
| `AMBIENT_TEMPERATURE` | Outside temperature |
| `MODULE_TEMPERATURE` | Solar panel temperature |
| `hour`, `day_of_week`, `is_daytime` | Time-based features |
| `AC_POWER_lag1`, `AC_POWER_lag2` | Lag features of power |
| `IRRADIATION_lag1`, `MODULE_TEMP_lag1` | Lag features of weather |

**Target Variable:** `AC_POWER`

---

## 🏗️ Project Structure

```bash
solar-power-forecasting/
│
├── data/                       # Raw & processed data
├── notebooks/                  # Jupyter notebooks
│   └── solar_forecasting.ipynb
├── models/                     # Saved models
│   └── solar_power_xgboost_model.pkl
├── src/                        # Source code (optional)
├── images/                     # Graphs & visualizations
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Pandas & NumPy** — Data processing
- **Matplotlib & Seaborn** — Visualization
- **Scikit-learn** — Baseline models & metrics
- **XGBoost & LightGBM** — Advanced gradient boosting
- **Joblib** — Model serialization

---

## 📈 Model Performance

### 1. With Current Irradiation (Nowcasting)

| Model              | MAE     | RMSE    | R²     |
|--------------------|---------|---------|--------|
| Linear Regression  | 305.25  | 547.60  | 0.9953 |
| Random Forest      | 233.29  | 479.60  | 0.9964 |
| LightGBM           | 227.79  | 457.70  | 0.9967 |
| **XGBoost**        | **220.22** | **447.90** | **0.9968** |

### 2. Realistic Forecasting (Without Current Irradiation)

| Metric             | Value   |
|--------------------|---------|
| **R² Score**       | 0.9636  |
| **MAE**            | 784.23  |
| **RMSE**           | 1520.79 |

> 63.2% of predictions have absolute error less than 500.

### 3. Direct Multi-step Forecasting

| Horizon       | MAE     | RMSE    |
|---------------|---------|---------|
| t+1 (15 min)  | 1300.81 | 2502.99 |
| t+2 (30 min)  | 1428.45 | 2664.22 |
| t+3 (45 min)  | 1490.43 | 2712.72 |
| t+4 (60 min)  | 1611.86 | 2977.23 |

---

## 🔍 Key Insights

- **Night time performance** is excellent (almost perfect zero predictions).
- Model performs best during low to medium power ranges.
- Highest errors occur during sudden power spikes (cloud movements).
- Current irradiation is the most dominant feature.
- Without future weather data, longer horizon forecasting becomes significantly harder.

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/solar-power-forecasting.git
cd solar-power-forecasting
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the dataset
```python
import kagglehub
path = kagglehub.dataset_download("anikannal/solar-power-generation-data")
```

### 4. Run the notebook
Open `notebooks/solar_forecasting.ipynb` and run all cells.

---

## 📦 Requirements

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
lightgbm
joblib
kagglehub
```

---

## 🧠 Future Improvements

- [ ] Integrate real-time weather forecast API (Open-Meteo / OpenWeather)
- [ ] Add Quantile Regression for prediction intervals
- [ ] Build Streamlit / Gradio web application
- [ ] Deploy model using FastAPI
- [ ] Test generalization on Plant 2 data
- [ ] Implement probabilistic forecasting

---

## ✍️ Author

**Saud Ahmad**  
Machine Learning Enthusiast | Data Science

- GitHub: [src_xenon](https://github.com/Saudahmd)
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/saudahmd10/)

---

## 📄 License

This project is licensed under the MIT License.
```
