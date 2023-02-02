from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException

from pydantic import BaseModel

from parser import full_name_parser

app = FastAPI()


class ParsedNameResponse(BaseModel):
    first_name: str
    last_name: str


@app.get("/")
async def another_parse():
    return "Welcome to the Name Parser!"


@app.get("/v1/parse", response_model=ParsedNameResponse, status_code=status.HTTP_200_OK)
async def parse_name(full_name: str) -> ParsedNameResponse:
    full_name = full_name.strip()
    if len(full_name) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="full_name cannot be empty!"
        )
    first_name, last_name = full_name_parser(full_name)

    return ParsedNameResponse(
        first_name=first_name.title(), last_name=last_name.title()
    )
