import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb
from datetime import timedelta

st.title("📦 Order Volume Forecasting App")
st.write("Predicts the total number of orders for the day (total_orders) based on data available up to a certain time.")

# モデルの読み込み
model = joblib.load("model1.pkl")

# データ読み込み
df = pd.read_csv("fake_pizza_orders_extended.csv")

# 日付と時間の選択
selected_date = st.selectbox("📅 Select the date", sorted(df["date"].unique()))
                             
selected_hour = st.slider("⏰ Data up to what time?", min_value=8, max_value=17, value=10)

# 対象日のデータ取得
filtered = df[(df["date"] == selected_date) & (df["hour"] <= selected_hour)]

if not filtered.empty:
    # 最新行を取得
    latest = filtered.sort_values("hour").iloc[-1]

    # 特徴量（モデルに合わせて変更）
    feature_cols = [
        'hour', 'orders', 'cumulative_orders', 'year', 'month', 'day', 'order_trend', 	
    'dayofweek_Friday', 'dayofweek_Monday', 'dayofweek_Saturday', 'dayofweek_Sunday', 
    'dayofweek_Thursday', 'dayofweek_Tuesday', 'dayofweek_Wednesday','is_weekend'
    ]
    X = latest[feature_cols].values.reshape(1, -1)

    # 予測
    pred = model.predict(X)[0]

    # 昨日の最終注文数を取得（前日比用）
    y_date = (pd.to_datetime(selected_date) - timedelta(days=1)).strftime("%Y-%m-%d")
    y_data = df[df["date"] == y_date]
    y_final = y_data["orders"].sum() if not y_data.empty else None

    # 手入力：仕掛かり数（バックログ）と出荷計画
    in_progress = st.number_input("🔄 BL in the mornig", min_value=0, step=1)
    shipment_plan = st.number_input("🗓️ today's shipments", min_value=0, step=1)

    # 合計予測出荷数
    total_forecast = pred + in_progress

    # 前日比
    diff_pct = (pred - y_final) / y_final * 100 if y_final else None
    
    backlog17 = shipment_plan - total_forecast


    # 結果表示
    st.subheader("📈 Result")
    col1, col2, col3, col4, col5= st.columns(5)
    col1.metric("① Final Predicted Orders", int(pred), f"{diff_pct:+.1f}%" if diff_pct else "N/A")
    col2.metric("② BL", int(in_progress))
    col3.metric("③ Predicted BL", int(total_forecast))
    col4.metric("④ Ship Plan", int(shipment_plan))
    col5.metric("⑤ Latest BL", int())
else:
    st.warning("Data is not found")

# 特徴量重要度の表示（オプション）
if st.checkbox("🧠 Display feature importance"):
    importances = model.feature_importances_
    feat_df = pd.DataFrame({"Feature": feature_cols, "Importance": importances})
    feat_df = feat_df.sort_values(by="Importance", ascending=False)
    st.bar_chart(feat_df.set_index("Feature"))
