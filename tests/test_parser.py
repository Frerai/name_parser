import pytest

from hypothesis import strategies as st
from hypothesis import given

from app.parser import full_name_parser


@pytest.mark.parametrize(
    "full_name, expected_name",
    [
        ("john doe", ("John", "Doe")),
        ("doe, john", ("John", "Doe")),
        ("Hans-Christian Jensen", ("Hans-Christian", "Jensen")),
        ("P. H. Kristensen", ("P. H.", "Kristensen")),
        ("Peter Hans Kristensen", ("Peter Hans", "Kristensen")),
        ("Kristensen, P. H.", ("P. H.", "Kristensen")),
        (",", (",", "")),
        ("", ("", "")),
        ("Ærløng Åssesens Søns-Sønnesen", ("Ærløng Åssesens", "Søns Sønnesen")),
        ("Daniel", ("Daniel", "")),
        ("Chow-mein-noodles Dim-Sum Ting", ("Chow-Mein-Noodles Dim-Sum", "Ting")),
    ],
)
def test_parser(full_name: str, expected_name: str) -> None:
    """Tests that parser will parse various combinations of a full name
    correctly as intended, with or without containing symbols, and returns
    names formated as first name and last name.

    Pytest will allow tests to be parameterized in any way desired."""
    assert expected_name == full_name_parser(full_name)


@given(
    # Allows for all Characters (L). This includes  lowercase (Ll), modifier (Lm),
    # titlecase (Lt), uppercase (Lu), other (Lo).
    st.text(alphabet=st.characters(whitelist_categories=("L",)), min_size=1),
    st.text(
        alphabet=st.characters(whitelist_categories=("Zs",)), min_size=1
    ),  # Allows for spaces (Zs).
    st.text(alphabet=st.characters(whitelist_categories=("L",)), min_size=1),
)
def test_parser_with_hypothesis_randomly_generated_characters(
        given_first_name: str, given_symbol: str, given_last_name: str
) -> None:
    """Tests that parser will handle any combination of letters and
    characters to pass the parsing.
    Added randomly generated spaces. Parsing trims any amount of spacing.

    Hypothesis will automatically generate fields in any way defined."""

    full_name = f"{given_first_name} {given_symbol} {given_last_name}"
    formatted_data = full_name_parser(full_name)

    assert given_first_name.title() == formatted_data[0]
    assert given_last_name.title() == formatted_data[1]
    assert given_symbol not in formatted_data
