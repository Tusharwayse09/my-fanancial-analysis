from scripts.fetch_api import load_company_ids, fetch_company_data
from scripts.financial_metrics import extract_financial_metrics
from scripts.analysis import analyze_company
from scripts.db_store import store_ml_result

def run_pipeline():
    print("RUN.PY STARTED")
    company_ids = load_company_ids()

    success = 0
    failed = 0

    print(f"\nTOTAL COMPANIES FOUND: {len(company_ids)}")
    print("=" * 60)

    for index, company_id in enumerate(company_ids, start=1):
        print(f"\n[{index}/{len(company_ids)}] Processing: {company_id}")

        try:
            api_response = fetch_company_data(company_id)
            metrics = extract_financial_metrics(api_response)

            pros, cons = analyze_company(
                metrics["sales_growth_5y"],
                metrics["profit_growth_5y"],
                metrics["roe"]
            )

            store_ml_result(company_id, metrics, pros, cons)
            success += 1

            print(f"✅ {company_id} processed successfully")

        except Exception as e:
            failed += 1
            print(f"❌ Failed for {company_id}: {e}")

    print("\n" + "=" * 60)
    print("BATCH PROCESS COMPLETED")
    print(f"SUCCESSFUL: {success}")
    print(f"FAILED: {failed}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()
