import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb
from datetime import timedelta

# モデル読み込み
model = joblib.load("model1.pkl")

# データ読み込み
df = pd.read_csv("fake_pizza_orders_extended.csv")

# 🔧 前処理関数
def preprocess(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["dayofweek"] = df["date"].dt.day_name()
    df["is_weekend"] = df["dayofweek"].isin(["Saturday", "Sunday"]).astype(int)
    df["cumulative_orders"] = df.groupby("date")["orders"].cumsum()
    df["order_trend"] = df.groupby("date")["orders"].diff().fillna(0)
    dummies = pd.get_dummies(df["dayofweek"], prefix="dayofweek")
    df = pd.concat([df, dummies], axis=1)
    return df

# 前処理実行
df = preprocess(df)

# UI表示
st.title("🍕 Order Forecast Dashboard")

# カラム確認（デバッグ用）
# st.write("Columns in the dataframe:", df.columns)

# 日付と時間の選択
selected_date = st.selectbox("📅 Select the date", sorted(df["date"].dt.strftime("%Y-%m-%d").unique()))
selected_hour = st.slider("⏰ Data up to what time?", min_value=8, max_value=17, value=10)

# 対象日のデータ取得
filtered = df[(df["date"].dt.strftime("%Y-%m-%d") == selected_date) & (df["hour"] <= selected_hour)]

if not filtered.empty:
    latest = filtered.sort_values("hour").iloc[-1]

    # モデルに必要な特徴量
    feature_cols = [
        'hour', 'orders', 'cumulative_orders', 'year', 'month', 'day', 'order_trend',
        'dayofweek_Friday', 'dayofweek_Monday', 'dayofweek_Saturday',
        'dayofweek_Sunday', 'dayofweek_Thursday', 'dayofweek_Tuesday',
        'dayofweek_Wednesday', 'is_weekend'
    ]

    # 欠損カラムを補う（0埋め）
    for col in feature_cols:
        if col not in latest:
            latest[col] = 0

    # 予測
    X = latest[feature_cols].values.reshape(1, -1)
    pred = model.predict(X)[0]

    # 昨日の最終注文数を取得（前日比）
    y_date = (pd.to_datetime(selected_date) - timedelta(days=1)).strftime("%Y-%m-%d")
    y_data = df[df["date"].dt.strftime("%Y-%m-%d") == y_date]
    y_final = y_data["orders"].sum() if not y_data.empty else None

    # 手入力：バックログと出荷計画
    in_progress = st.number_input("🔄 BL in the morning", min_value=0, step=1)
    shipment_plan = st.number_input("🗓️ Today's shipments", min_value=0, step=1)

    # 合計予測出荷数
    total_forecast = pred + in_progress

    # 前日比計算
    diff_pct = (pred - y_final) / y_final * 100 if y_final else None

    # 17時時点の残BL予測
    backlog17 = total_forecast - shipment_plan

    # 結果表示
    st.subheader("📈 Result")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("① Final Orders", int(pred), f"{diff_pct:+.1f}%" if diff_pct is not None else "N/A")
    col2.metric("② BL (Morning)", int(in_progress))
    col3.metric("③ Predicted BL", int(total_forecast))
    col4.metric("④ Shipment Plan", int(shipment_plan))
    col5.metric("⑤ BL at 17:00", int(backlog17))
else:
    st.warning("⚠️ No data found for the selected date and time.")



