# 🍕 Order Forecasting App (Streamlit + XGBoost)

This app forecasts daily order volume for a pizza delivery operation using an XGBoost model and a real-time Streamlit dashboard.

## 🔧 Features

- Predicts end-of-day order volume based on cumulative data up to a given hour.
- Accepts manual inputs for backlog and shipment plans.
- Displays current and predicted backlog, with day-over-day comparison.
- Suitable for warehouse or operations planning.

## 🖼️ App Overview

- Select a date and hour to analyze
- The model predicts final `orders` using XGBoost
- You can input:
  - Morning backlog (`BL`)
  - Planned shipments for the day
- The app calculates:
  - Predicted final orders
  - Combined `orders + backlog`
  - Estimated backlog at 5pm

## 🧪 Model Info

- Model: XGBoost Regressor
- Trained on: `fake_pizza_orders_extended.csv`
- Input features include:
  - Time (`hour`, `cumulative_orders`, `order_trend`)
  - Date decomposition (`year`, `month`, `day`, `dayofweek`, `is_weekend`)
  - One-hot encoded weekdays

## 📁 File Structure

| File | Description |
|------|-------------|
| `app.py` | Streamlit main script |
| `model1.pkl` | Trained XGBoost model |
| `fake_pizza_orders_extended.csv` | Input data for the app |
| `requirements.txt` | Python dependencies |
| `README.md` | This documentation |

## ✅ Installation

```bash
git clone https://github.com/yourusername/order-prediction-app.git
cd order-prediction-app
pip install -r requirements.txt
streamlit run app.py
>>>>>>> repoA/main
