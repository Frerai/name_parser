from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException

import emoji

from app.models.responses import ParsedNameResponse
from app.parser import full_name_parser
from app.parser import validate_input


router = APIRouter()


@router.get("/parse", response_model=ParsedNameResponse, status_code=status.HTTP_200_OK)
async def parse_short_name(full_name: str) -> ParsedNameResponse:
    """Router to the name parser endpoint. A successful response: status code 200.
    This response depends on the custom model ParsedNameResponse to enter the users
    input string.
    The name parser endpoint does not correctly handle inputs with middle names."""
    full_name = full_name.strip()
    if len(full_name) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="full_name cannot be empty!"
        )
    first_name, last_name = full_name_parser(full_name)

    if validate_input(full_name):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="no use of emojis allowed!"
        )

    return ParsedNameResponse(
        first_name=first_name.title(), last_name=last_name.title()
    )
