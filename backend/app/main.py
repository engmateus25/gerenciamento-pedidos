from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from app.db import engine
from app.models import models
from app.routes import tables, menu_items, orders


models.Base.metadata.create_all(bind=engine)

app = FastAPI()  


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


app.include_router(tables.router)
app.include_router(menu_items.router)
app.include_router(orders.router)


@app.get("/")
def root():
    return {"message": "API funcionando gente!"}
