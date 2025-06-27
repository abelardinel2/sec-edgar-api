import os
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from sec_edgar_downloader import Downloader
from datetime import datetime
import uvicorn

app = FastAPI()

company_name = os.getenv("COMPANY_NAME")
email = os.getenv("SEC_EMAIL")

dl = Downloader(company_name, email)

@app.get("/api/v1/insider-trades")
def get_insider_trades(ticker: str = Query(..., min_length=1)):
    cik = dl.lookup_cik(ticker.upper())
    filings = dl.get("4", cik)
    return {"ticker": ticker.upper(), "form4_count": len(filings)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)