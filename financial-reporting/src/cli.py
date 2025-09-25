"""Simple CLI entrypoint for the project."""

import os
import sys

def main():
    print("Welcome to Financial Reporting skeleton.")
    print("Edit src/ to implement ingestion, ETL and reporting.")
    print("Examples:")
    print("  python -m src.cli fetch_prices AAPL")
    print("  python -m src.cli ingest_csv data/sample.csv AAPL")
    sys.exit(0)

if __name__ == "__main__":
    main()
