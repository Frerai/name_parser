def full_name_parser(full_name: str):
    # TODO add comments
    parts = full_name.split()
    if len(parts) == 0:
        return "", ""
    if len(parts) == 1:
        first_name = parts[0]
        last_name = ""
    elif "," in full_name:
        last_name, first_name = [part.strip() for part in full_name.split(",")]
    elif "-" in parts[-1]:
        first_name = " ".join(parts[:-1])
        last_name = parts[-1].replace("-", " ")
    else:
        first_name = " ".join(parts[:-1])
        last_name = parts[-1]
    return first_name.title(), last_name.title()
