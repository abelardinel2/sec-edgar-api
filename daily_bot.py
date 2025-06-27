
import os
from sec_edgar_downloader import Downloader

company_name = os.getenv("COMPANY_NAME")
email = os.getenv("SEC_EMAIL")

dl = Downloader(company_name, email)

# Get Form 4 filings for AAPL
filings = dl.get("4", "AAPL")
print(f"Downloaded filings: {filings}")
