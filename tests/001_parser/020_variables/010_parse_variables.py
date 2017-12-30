# -*- coding: utf-8 -*-
import os
import pytest

from boussole.parser.variables import ScssVariablesParser


@pytest.mark.parametrize("source,attempted", [
    (
        """// $foo: bar;""",
        []
    ),
    (
        (
            """$ok: yop;\n"""
            """// $nope: "commented";\n"""
            """$yep: yip;\n"""
        ),
        [
            ("$ok", "yop"),
            ("$yep", "yip"),
        ]
    )
])
def test_parser_flaws(source, attempted):
    """Just testing commented variables are not retained"""
    parser = ScssVariablesParser()

    result = parser.parse(source)

    assert [item.groups() for item in result] == attempted
