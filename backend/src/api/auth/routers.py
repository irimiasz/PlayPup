from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/users", status_code=201)
async def register():
    return JSONResponse({"you_are": "registered"})
