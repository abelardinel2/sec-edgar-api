import os
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from sec_edgar_downloader import Downloader
from datetime import datetime
import uvicorn
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Validate environment variables
company_name = os.getenv("COMPANY_NAME")
email = os.getenv("SEC_EMAIL")
if not company_name or not email:
    raise ValueError("COMPANY_NAME and SEC_EMAIL must be set in the environment")

try:
    dl = Downloader(company_name, email)
    logger.info("Downloader initialized successfully")
except TypeError as e:
    logger.error(f"Failed to initialize Downloader: {e}")
    raise

@app.get("/api/v1/insider-trades")
def get_insider_trades(ticker: str = Query(..., min_length=1)):
    try:
        cik = dl.lookup_cik(ticker.upper())
        filings = dl.get("4", cik)  # Adjust based on actual library behavior
        filtered = [
            f"Form 4 filed on {f['date_filed']} for {ticker.upper()}"
            for f in filings
        ]
        return JSONResponse(content={
            "ticker": ticker.upper(),
            "cik": cik,
            "form4_count": len(filtered),
            "date_checked": datetime.now().strftime("%Y-%m-%d"),
            "trades": filtered
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)