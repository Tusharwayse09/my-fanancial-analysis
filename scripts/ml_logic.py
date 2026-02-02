def generate_pros_cons(metrics):
    pros = []
    cons = []

    # Sales Growth
    if metrics["sales_growth_5y"] > 10:
        pros.append(
            f"Company has delivered good sales growth of {metrics['sales_growth_5y']}% over the last 5 years."
        )
    else:
        cons.append(
            f"Company has delivered poor sales growth of {metrics['sales_growth_5y']}% over the last 5 years."
        )

    # Profit Growth
    if metrics["profit_growth_5y"] > 10:
        pros.append(
            f"Company has delivered strong profit growth of {metrics['profit_growth_5y']}% over the last 5 years."
        )
    else:
        cons.append(
            f"Company has delivered weak profit growth of {metrics['profit_growth_5y']}% over the last 5 years."
        )

    # ROE
    if metrics["roe"] > 10:
        pros.append(
            f"Company has a healthy ROE of {metrics['roe']}%."
        )
    else:
        cons.append(
            f"Company has a low ROE of {metrics['roe']}%."
        )

    # Dividend Payout
    if metrics["dividend_payout"] > 10:
        pros.append(
            f"Company has a good dividend payout of {metrics['dividend_payout']}%."
        )
    else:
        cons.append(
            f"Company has a low dividend payout of {metrics['dividend_payout']}%."
        )

    # 🔴 ENSURE AT LEAST ONE CON
    if not cons:
        cons.append(
            "After strong historical performance, future growth may moderate."
        )

    # Limit results
    return pros[:3], cons[:3]
