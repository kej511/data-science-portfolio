# 🔋 Electricity Power Consumption Forecast

This project provides a machine learning-based prediction system for household electricity power consumption using an XGBoost regression model. It includes both a web-based UI with Streamlit and an API interface using FastAPI.

---

## 📦 Project Structure

. ├── streamlit_app.py # Streamlit frontend for user input and prediction ├── fastapi_app.py # FastAPI backend for API access ├── xgboost_model.pkl # Trained XGBoost regression model ├── README.md # This file └── requirements.txt # Python dependencies


## 🎯 Objective

Predict the next day’s **Global Active Power (kW)** consumption based on various features including voltage, reactive power, time-related values, and lag-based features.

---

## 📈 Model Details

- **Algorithm**: XGBoost Regressor
- **Input Features**:
  - Voltage
  - Global Reactive Power
  - Global Intensity
  - Sub_metering_1 / 2 / 3
  - Year, Month, Day, Day of Week
  - Lag1, Lag7, Rolling Mean (7 days)
- **Target Variable**: Global Active Power (kW)
- **Training Dataset**: Processed household electric power consumption data

---

## 🔮 Latest Prediction Example

- **Date**: 2025-04-08
- **Input**: Averaged feature values  
- **Prediction Result**: `1.0388 kW`

---

## 🚀 Usage

#### ▶️ 1. Streamlit App (Interactive UI)

```bash
streamlit run streamlit_app.py
Access via browser at: http://localhost:8501

Enter feature values manually to get real-time predictions

#### ⚡ 2. FastAPI App (API Access)

uvicorn fastapi_app:app --reload
Access Swagger UI: http://127.0.0.1:8000/docs

POST request endpoint:

/predict
Example input:
{
  "Voltage": 240.0,
  "Global_reactive_power": 0.2,
  "Global_intensity": 4.0,
  ...
}
🛠 Future Ideas
⏱ Add scheduler to predict daily usage automatically

📊 Visualize prediction trends over time

🧠 Implement model retraining pipeline with new data

📡 Connect with smart meter for real-time input

📚 Requirements

streamlit
fastapi
uvicorn
pandas
numpy
xgboost
pickle-mixin
Install via:

pip install -r requirements.txt

📝 License
This project is open-source and available under the MIT License.
