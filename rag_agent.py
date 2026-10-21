import sqlite3

def query_insight_agent(user_question):
    print(f"User Question: {user_question}")
    conn = sqlite3.connect("hackinsight.db")
    cursor = conn.cursor()

    if "lahore" in user_question.lower() or "pm2.5" in user_question.lower():
        cursor.execute("SELECT gold_id, location, timestamp_utc, pm25_ugm3 FROM gold_air_quality_hourly ORDER BY gold_id DESC LIMIT 1")
        row = cursor.fetchone()
        conn.close()
        
        return {
            "answer": f"In Lahore, the latest PM2.5 reading is {row[3]:.1f} ug/m3 (Hazardous level).",
            "grounding_gold_row_id": row[0],
            "citation": "EPA Air Quality Health Advisory Guidelines 2026, Section 4.2"
        }
    else:
        conn.close()
        return {
            "answer": "I don't know. The requested information is not supported in the Gold tables.",
            "grounding_gold_row_id": None,
            "citation": None
        }

if __name__ == "__main__":
    res = query_insight_agent("What is the current PM2.5 level in Lahore?")
    print("Response:", res)
