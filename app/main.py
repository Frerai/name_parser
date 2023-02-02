from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException

from app.utils import full_name_parser
from app.models.writers import ParsedNameResponse

app = FastAPI()


@app.get("/v1")
async def another_parse():
    """Router to the frontpage."""
    return "Welcome to the Name Parser!"


@app.get("/v1/parse", response_model=ParsedNameResponse, status_code=status.HTTP_200_OK)
async def parse_name(full_name: str) -> ParsedNameResponse:
    """Router to name parser."""
    full_name = full_name.strip()
    if len(full_name) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="full_name cannot be empty!"
        )
    first_name, last_name = full_name_parser(full_name)

    return ParsedNameResponse(
        first_name=first_name.title(), last_name=last_name.title()
    )
