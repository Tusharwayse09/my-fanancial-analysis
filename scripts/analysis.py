from scripts.ml_prediction import predict_future_growth


def analyze_company(sales_growth, profit_growth, roe):
    pros = []
    cons = []

    # PROS
    if sales_growth > 20:
        pros.append(f"Strong sales growth of {sales_growth}% over last 5 years.")
    if profit_growth > 30:
        pros.append(f"Healthy profit growth of {profit_growth}% over last 5 years.")
    if roe > 15:
        pros.append(f"Good return on equity (ROE) of {roe}%.")

    # CONS
    if roe < 10:
        cons.append("Low ROE indicates inefficient capital usage.")
    if sales_growth < 10:
        cons.append("Sales growth is relatively weak.")
    if not cons:
        cons.append("Future growth may stabilize after strong performance.")

    # 🔮 ML PREDICTION (Dummy historical trend)
    sales_history = [sales_growth - 10, sales_growth - 5, sales_growth]
    profit_history = [profit_growth - 15, profit_growth - 7, profit_growth]

    future_sales = predict_future_growth(sales_history)
    future_profit = predict_future_growth(profit_history)

    pros.append(
        f"ML forecast suggests sales growth may reach ~{future_sales[-1]}% in coming years."
    )
    pros.append(
        f"ML forecast suggests profit growth may reach ~{future_profit[-1]}% in coming years."
    )

    return pros, cons
