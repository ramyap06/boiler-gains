from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import crud

# initializing the API
app = FastAPI(
    title="Boiler Gains API",
    description="api to store backend for boiler gains web app",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# create a REST API by defining endpoint & reading root
@app.get("/")
def read_root():
    return 0

@app.get("/items")
def get_all_items():
    return crud.get_all()

@app.post("/items")
def create_item(item: dict):
    return crud.post(item)

@app.get("/items/{item_id}")
def get_item(item_id: str):
    return crud.get(item_id)

@app.put("/items/{item_id}")
def update_item(item_id: str, item_dict: dict):
    row = crud.put(item_id, item_dict)
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return row

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    deleted = crud.delete(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": True}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)