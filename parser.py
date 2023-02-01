def full_name_parser(full_name):
    # TODO add comments
    if "," in full_name:
        last_name, first_name = full_name.split(", ")

    else:
        names = full_name.split(" ")
        last_name = names[-1]
        first_name = " ".join(names[:-1])

    return first_name, last_name
