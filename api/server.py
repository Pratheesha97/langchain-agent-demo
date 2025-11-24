from fastapi import FastAPI

app = FastAPI(
    title="LangChain Agent Demo API",
    description="Simple REST API for Stage 2 demonstration",
    version="1.0.0"
)

@app.get("/public-info")
def public_info():
    return {
        "service": "LangChain Agent Demo API",
        "message": "This is the public info endpoint.",
        "status": "running"
    }


@app.get("/sales")
def sales():
    return {
        "sales": [
            {"region": "US", "amount": 1200},
            {"region": "EU", "amount": 1800},
            {"region": "APAC", "amount": 2400},
        ],
        "currency": "USD"
    }
