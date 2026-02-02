import requests
import pandas as pd
from config import API_BASE_URL, API_KEY


def load_company_ids():
    """
    Reads company IDs from Excel file provided by the company
    """
    df = pd.read_excel(
        "data/company_id.xlsx",
        engine="openpyxl"
    )
    return df["company_id"].dropna().tolist()


def fetch_company_data(company_id):
    """
    Fetch financial data for a single company from API
    """
    params = {
        "id": company_id,
        "api_key": API_KEY
    }

    response = requests.get(API_BASE_URL, params=params, timeout=20)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    company_ids = load_company_ids()

    # Test only the first company
    first_company = company_ids[0]
    print(f"Testing company: {first_company}")

    data = fetch_company_data(first_company)

    print("\nAPI RESPONSE:")
    print(data)
