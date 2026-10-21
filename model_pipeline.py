import sqlite3
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

def train_and_evaluate():
    print("Training Model vs Declared Baseline...")
    conn = sqlite3.connect("hackinsight.db")
    df = pd.read_sql("SELECT * FROM gold_air_quality_hourly LIMIT 10000", conn)
    conn.close()

    df["pm25_lag24"] = df["pm25_ugm3"].shift(24)
    df.dropna(inplace=True)

    split_idx = int(len(df) * 0.8)
    train, test = df.iloc[:split_idx], df.iloc[split_idx:]

    X_train, y_train = train[["pm25_lag24"]], train["pm25_ugm3"]
    X_test, y_test = test[["pm25_lag24"]], test["pm25_ugm3"]

    baseline_pred = test["pm25_lag24"]
    baseline_mae = mean_absolute_error(y_test, baseline_pred)

    model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    model_pred = model.predict(X_test)
    model_mae = mean_absolute_error(y_test, model_pred)

    print(f"Baseline (Persistence) MAE: {baseline_mae:.2f} ug/m3")
    print(f"Model (Gradient Boosting) MAE: {model_mae:.2f} ug/m3")
    print(f"MAE Improvement: {((baseline_mae - model_mae)/baseline_mae)*100:.1f}%")

if __name__ == "__main__":
    train_and_evaluate()
