import pytest

from parser import full_name_parser


@pytest.mark.parametrize("full_name, expected_name", [
    ("john doe", ("John", "Doe")),
    ("doe, john", ("John", "Doe")),
    ("Hans-Christian Jensen", ("Hans-Christian", "Jensen")),
    ("P. H. Kristensen", ("P. H.", "Kristensen")),
    ("Peter Hans Kristensen", ("Peter Hans", "Kristensen")),
    ("Kristensen, P. H.", ("P. H.", "Kristensen")),
    (",", (",", "")),
    ("Ærløng Åssesens Søns-Sønnesen", ("Ærløng Åssesens", "Søns Sønnesen")),
    ("Daniel", ("Daniel", "")),
    ("Chow-mein-noodles Dim-Sum Ting", ('Chow-Mein-Noodles Dim-Sum', 'Ting'))
]
     )
def test_parser(full_name, expected_name):
    assert expected_name == full_name_parser(full_name)


