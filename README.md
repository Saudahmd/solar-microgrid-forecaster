# ⚡ Solar Micro-Grid Power Generation & Deficit Forecaster

### Intelligent Multi-Step Forecasting System for Solar Microgrids

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Latest-orange)](https://xgboost.readthedocs.io/)
[![LightGBM](https://img.shields.io/badge/LightGBM-Latest-green)](https://lightgbm.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An end-to-end machine learning pipeline and interactive operations console designed for utility-scale solar generation forecasting and microgrid deficit safeguarding. 

Built with **LightGBM**, **Streamlit**, and **Plotly**, the system models multi-quantile prediction intervals ($p_{10}, p_{50}, p_{90}$) to generate proactive battery storage (BESS) dispatch schedules and mitigate costly microgrid power deficits.

---

## 🎯 Overview & Operational Problem

Solar generation is inherently intermittent, fluctuating with ambient temperature, cloud cover, and seasonal shifts. In hybrid microgrids and industrial solar plants, unpredicted generation drops force sudden reliance on expensive diesel fallback generators or lead to brownouts.

This project addresses the operational challenge by:
- Moving beyond single-point estimates to **probabilistic forecasting** ($p_{10}, p_{50}, p_{90}$).
- Heavily safeguarding against underprediction risk using a conservative $p_{10}$ floor for battery reserve guarantees.
- Translating real-time telemetry into actionable battery energy storage (BESS) charge/discharge recommendations.

---

## 🚀 Key Features

- **Physics-Informed Feature Engineering:** Incorporates photovoltaic (PV) thermal derating formulas (efficiency degradation above 25°C), cyclical solar time encodings, and rolling irradiance volatility.
- **Probabilistic Quantile Modeling:** Uses LightGBM quantile regression to output median forecasts alongside conservative generation floors and curtailment ceilings.
- **Strict Chronological Evaluation:** Evaluated on a 120-hour out-of-sample holdout test to prevent lookahead data leakage.
- **Interactive Operations Console:** Built with Streamlit and Plotly to simulate base-load stress, visualize prediction bands, and compute avoided diesel fallback costs in real time.

---

## 📊 Benchmark Model Performance

Tested across an out-of-sample 120-hour evaluation horizon:

| Metric | Score | Operational Significance |
| :--- | :--- | :--- |
| **R² Score** | **0.9962** | Explains 99.6% of diurnal variance in generation. |
| **WAPE** | **4.26%** | Total volume forecast error rate (95.74% overall accuracy). |
| **MAE** | **268.23 kW** | Average deviation (~1% of aggregate plant capacity). |
| **PICP (80% Band)** | **70.83%** | Empirical coverage between $p_{10}$ and $p_{90}$ intervals. |

---

## 🛠️ Tech Stack

- **Language & Core:** Python, Pandas, NumPy
- **Machine Learning:** LightGBM, Scikit-Learn
- **Visualization & UI:** Streamlit, Plotly
- **Deployment:** Streamlit Community Cloud

---

## 💻 Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Saudahmd/solar-microgrid-forecaster.git](https://github.com/Saudahmd/solar-microgrid-forecaster.git)
   cd solar-microgrid-forecaster

## ✍️ Author

**Saud Ahmad**  
Machine Learning Enthusiast | Data Science

- GitHub: [Saud-Ahmad](https://github.com/Saudahmd)
- LinkedIn: [Saud-Ahmad-10](https://www.linkedin.com/in/saudahmd10/)

---

## 📄 License

This project is licensed under the MIT License.
```
