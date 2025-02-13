import uvicorn
from fastapi import FastAPI
from routes import health, metrics

app = FastAPI()

app.include_router(health.router)
app.include_router(metrics.router)

@app.get("/")
def root():
    return {"message": "Hello World!!!"}

if __name__ == "__main__":
    uvicorn.run("api_router:app", reload=True)
