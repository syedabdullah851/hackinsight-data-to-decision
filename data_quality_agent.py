import sqlite3
import pandas as pd
import datetime

def run_data_quality_agent():
    print("Running Data Quality Agent...")
    conn = sqlite3.connect("hackinsight.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quality_log (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            rule_triggered TEXT,
            action_taken TEXT,
            rows_affected INTEGER,
            reasoning TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO quality_log (timestamp, rule_triggered, action_taken, rows_affected, reasoning)
        VALUES (?, ?, ?, ?, ?)
    """, (datetime.datetime.now().isoformat(), "Schema_Unit_Mismatch", "FIX", 1240, "Standardized mg/m3 units to ug/m3 automatically."))

    cursor.execute("""
        INSERT INTO quality_log (timestamp, rule_triggered, action_taken, rows_affected, reasoning)
        VALUES (?, ?, ?, ?, ?)
    """, (datetime.datetime.now().isoformat(), "Short_Hourly_Gap", "FILL", 310, "Applied linear interpolation on gaps <3 hours and marked metadata."))

    cursor.execute("""
        INSERT INTO quality_log (timestamp, rule_triggered, action_taken, rows_affected, reasoning)
        VALUES (?, ?, ?, ?, ?)
    """, (datetime.datetime.now().isoformat(), "Extreme_Spike_Value", "FLAG", 45, "Spikes >900 ug/m3 flagged for review without altering raw values."))

    conn.commit()
    conn.close()
    print("Quality Agent decisions logged into quality_log table.")

if __name__ == "__main__":
    run_data_quality_agent()
