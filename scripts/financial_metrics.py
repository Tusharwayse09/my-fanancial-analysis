def _filter_yearly_data(pnl_data):
    """
    Remove TTM rows and sort data by year
    """
    yearly = [row for row in pnl_data if row["year"] != "TTM"]
    yearly.sort(key=lambda x: x["year"])
    return yearly


def _calculate_growth(old, new):
    if old == 0:
        return 0.0
    return round(((new - old) / old) * 100, 2)


def extract_financial_metrics(api_response):
    company = api_response["company"]
    data = api_response["data"]

    pnl = _filter_yearly_data(data["profitandloss"])

    # Use 5-year comparison if possible
    if len(pnl) >= 6:
        start = pnl[-6]
    else:
        start = pnl[0]

    end = pnl[-1]

    sales_growth_5y = _calculate_growth(
        float(start["sales"]),
        float(end["sales"])
    )

    profit_growth_5y = _calculate_growth(
        float(start["net_profit"]),
        float(end["net_profit"])
    )

    metrics = {
        "sales_growth_5y": sales_growth_5y,
        "profit_growth_5y": profit_growth_5y,
        "roe": float(company["roe_percentage"]),
        "dividend_payout": float(end["dividend_payout"]) if end["dividend_payout"] else 0.0
    }

    return metrics
