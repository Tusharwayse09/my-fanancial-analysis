from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

# -------------------------------
# Database Connection
# -------------------------------
def get_db_connection():
    conn = sqlite3.connect("finance.db")
    conn.row_factory = sqlite3.Row
    return conn


# -------------------------------
# Frontend Home Page
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# Get ALL Results (Raw Data)
# -------------------------------
@app.route("/results")
def get_all_results():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM ml").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])


# -------------------------------
# Get Single Company (Raw)
# -------------------------------
@app.route("/results/<company_id>")
def get_company(company_id):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM ml WHERE company_id = ?",
        (company_id.upper(),)
    ).fetchone()
    conn.close()

    if not row:
        return jsonify({"error": "Company not found"}), 404

    return jsonify(dict(row))


# -------------------------------
# 🔥 MAIN ANALYSIS API (FOR UI)
# -------------------------------
@app.route("/analyze/<company>")
def analyze_company(company):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT * FROM ml WHERE company_id = ?",
        (company.upper(),)
    ).fetchone()
    conn.close()

    if not row:
        return jsonify({"error": "Company not found"}), 404

    return jsonify({
        "company": row["company_id"],
        "sales_growth": row["sales_growth"],
        "profit_growth": row["profit_growth"],
        "roe": row["roe"],
        "pros": row["pros"].split(" | "),
        "cons": row["cons"].split(" | ")
    })


# -------------------------------
# App Start
# -------------------------------
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=False)
