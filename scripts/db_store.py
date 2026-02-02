import sqlite3

def store_ml_result(company_id, metrics, pros, cons):
    print("CONNECTING TO SQLITE DATABASE...")

    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ml (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id TEXT UNIQUE,
            sales_growth REAL,
            profit_growth REAL,
            roe REAL,
            pros TEXT,
            cons TEXT
        )
    """)

    cursor.execute("""
        INSERT OR REPLACE INTO ml (
            company_id,
            sales_growth,
            profit_growth,
            roe,
            pros,
            cons
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        company_id,
        metrics["sales_growth_5y"],
        metrics["profit_growth_5y"],
        metrics["roe"],
        " | ".join(pros),
        " | ".join(cons)
    ))

    conn.commit()
    conn.close()

    print("DATABASE INSERT DONE (SQLITE)")
