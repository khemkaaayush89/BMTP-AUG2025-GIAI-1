from fastapi import FastAPI
import uvicorn

# Create FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/square")
def square(number: int):
    return {"number": number, "square": number ** 2}

# Main entry point
def main():
    uvicorn.run(
        "main:app",          # points to app instance
        host="127.0.0.1",
        port=8000,
        reload=True          # enables auto-reload
    )

if __name__ == "__main__":
    main()
