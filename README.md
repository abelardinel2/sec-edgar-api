# 📊 SEC EDGAR Insider API

A lightweight FastAPI-based API that fetches insider trading data (Form 4 filings) from the SEC EDGAR system by stock ticker.

## 🚀 Features
- 🔍 Convert stock tickers to official SEC CIKs  
- 📄 Retrieve recent Form 4 filings  
- 📦 JSON-formatted responses  
- ⚡ Built with FastAPI — deploy anywhere  
- 🧠 Designed for integration with Telegram bots and dashboards

## 🛠 Usage

GET /api/v1/insider-trades?ticker=XYZ

## 🧪 Local Dev

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs)
