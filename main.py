from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/api/geckos/")
async def get_geckos(
    page: Optional[int] = None,
    name: Optional[str] = None,
    status: Optional[str] = None,
    gender: Optional[str] = None,
    species: Optional[str] = None
):

    return {
        "page": page,
        "name": name,
        "status": status,
        "gender": gender,
        "species": species
    }