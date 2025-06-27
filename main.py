import os
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from sec_edgar_downloader import Downloader
from datetime import datetime
import uvicorn

app = FastAPI()
dl = Downloader(f"CompanyName={os.getenv('COMPANY_NAME')}; EmailAddress={os.getenv('SEC_EMAIL')}")

@app.get("/api/v1/insider-trades")
def get_insider_trades(ticker: str = Query(..., min_length=1)):
    try:
        cik = dl.lookup_cik(ticker.upper())
        filings = dl.get("4", cik)
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
