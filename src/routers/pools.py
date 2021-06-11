from typing import List
from fastapi import APIRouter, status
import src.schemas.pool as schema

router = APIRouter(prefix="/pool", tags=["Pools"])

mock_pool = {"id": 1, "name": "Soft Pool", "location": "Citi Club, Indiranagar"}


@router.get("/", response_model=List[schema.Pool], status_code=status.HTTP_200_OK)
def list():
    return [mock_pool]


@router.get("/{id}", response_model=schema.Pool, status_code=status.HTTP_200_OK)
def show(id: int):
    return mock_pool


@router.post("/", response_model=schema.Pool, status_code=status.HTTP_201_CREATED)
def create(request: schema.CreatePool):
    return mock_pool


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
):
    return {"success": True, "message": "Deleted"}


@router.put("/{id}", response_model=schema.Pool, status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schema.Pool):
    return mock_pool
