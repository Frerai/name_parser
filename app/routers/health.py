from fastapi import APIRouter
from fastapi import status


router = APIRouter()


@router.get("/live", status_code=status.HTTP_204_NO_CONTENT)
async def liveness():
    """Endpoint to be used as liveness probe."""
