from pydantic import BaseModel


class ParsedNameResponse(BaseModel):
    """Class used for entering name to be parsed.
    When initiated, allows for first_name and last_name to be entered."""

    first_name: str
    last_name: str
