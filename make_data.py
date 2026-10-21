import sqlite3
import pandas as pd
import numpy as np
import datetime

def build_warehouse():
    print("Starting Data Warehouse Rebuild...")
    conn = sqlite3.connect("hackinsight.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS raw_air_quality (
            raw_id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            parameter TEXT,
            value REAL,
            unit TEXT,
            timestamp_utc TEXT,
            fetched_at TEXT
        )
    """)

    dates = pd.date_range(start="2020-01-01", end="2026-10-21", freq="h")
    n = len(dates)
    np.random.seed(42)
    
    pm25_vals = np.random.normal(loc=120, scale=40, size=n)
    pm25_vals = np.clip(pm25_vals, 5, 800)
    
    raw_df = pd.DataFrame({
        "location": np.random.choice(["Lahore_Central", "Karachi_South", "Peshawar_East"], size=n),
        "parameter": "pm25",
        "value": pm25_vals,
        "unit": np.random.choice(["ug/m3", "mg/m3"], size=n, p=[0.95, 0.05]),
        "timestamp_utc": dates.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    })
    
    raw_df.to_sql("raw_air_quality", conn, if_exists="replace", index=False)

    cleaned_df = raw_df.copy()
    mask_mg = cleaned_df['unit'] == 'mg/m3'
    cleaned_df.loc[mask_mg, 'value'] = cleaned_df.loc[mask_mg, 'value'] * 1000
    cleaned_df['unit'] = 'ug/m3'
    cleaned_df.to_sql("cleaned_air_quality", conn, if_exists="replace", index=False)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gold_air_quality_hourly (
            gold_id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            timestamp_utc TEXT,
            pm25_ugm3 REAL,
            health_risk_level TEXT,
            is_imputed INTEGER
        )
    """)
    
    gold_df = pd.DataFrame({
        "gold_id": np.arange(1, n + 1),
        "location": cleaned_df["location"],
        "timestamp_utc": cleaned_df["timestamp_utc"],
        "pm25_ugm3": cleaned_df["value"],
        "health_risk_level": np.where(cleaned_df["value"] > 150, "Hazardous", "Moderate"),
        "is_imputed": 0
    })
    
    gold_df.to_sql("gold_air_quality_hourly", conn, if_exists="replace", index_label="gold_id")
    conn.close()
    print("Warehouse successfully rebuilt!")

if __name__ == "__main__":
    build_warehouse()
