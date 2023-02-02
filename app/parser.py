from typing import Tuple


def full_name_parser(full_name: str) -> Tuple[str, str]:
    """Function for parsing names as full names and returns name parts
    as a tuple consisting of a first name and last name.

    :arg:
    full_name as input string in any way desired.

    :returns:
    The full name split in parts. Will return the name parts in a tuple
    as first name and last name.
    """
    # Splits the full name in parts of two.
    parts = full_name.split()

    if len(parts) == 0:
        # Checks if input string is empty. Error handling is done at router, in case of empty input.
        return "", ""

    if len(parts) == 1:
        # There is only a first name.
        first_name = parts[0]
        last_name = ""

    elif "," in full_name:
        # Checks for seperator. Will split the name, by occurrence of "," as last name and first name.
        last_name, first_name = [part.strip() for part in full_name.split(",")]

    elif "-" in parts[-1]:
        # Checks for "-" in last part. Last name is found by last index of parts.
        first_name = " ".join(parts[:-1])
        # Last name is found, and replace seperator with spaces to format properly.
        last_name = parts[-1].replace("-", " ")

    else:
        # Will combine first and second to last word in full name as first name(s).
        first_name = " ".join(parts[:-1])
        # Last name is last index of parts.
        last_name = parts[-1]

    return first_name.title(), last_name.title()
