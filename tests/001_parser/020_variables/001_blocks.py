# -*- coding: utf-8 -*-
import os
import pytest

from boussole.parser.variables import ScssVariablesParser


@pytest.mark.parametrize("source", [
    """.selector{ color: $color; }""",
    """#id{ font: Arial 12px; }""",
    """nope: #000;""",
    """$color;""",
    """$color:""",
])
def test_nonvariable_blocks(source):
    """Non variable rules"""
    parser = ScssVariablesParser()

    result = parser.parse(source)

    assert [item.groups() for item in result] == []


@pytest.mark.xfail
@pytest.mark.parametrize("source", [
    """// $foo: bar;""", # Regex cannot ignore commented variable
])
def test_parser_flaws(source):
    """Some flaw that should be fixed, at least keeped as reference"""
    parser = ScssVariablesParser()

    result = parser.parse(source)

    assert [item.groups() for item in result] == []


@pytest.mark.parametrize("source,attempted", [
    (
        """$color: #ffffff;""",
        [
            ('color', '#ffffff'),
        ],
    ),
    (
        """$empty:;""",
        [
            ('empty', ''),
        ],
    ),
    (
        """$quote: 'cot';""",
        [
            ('quote', "'cot'"),
        ],
    ),
    (
        """$doublequote: "cot";""",
        [
            ('doublequote', '"cot"'),
        ],
    ),
    (
        """$operation: $foo / 42;""",
        [
            ('operation', '$foo / 42'),
        ],
    ),
    (
        """$breakpoint: unquote("screen and #{breakpoint(medium)}");""",
        [
            ('breakpoint', 'unquote("screen and #{breakpoint(medium)}")'),
        ],
    ),
    (
        """$list: foo bar;""",
        [
            ('list', 'foo bar'),
        ],
    ),
    (
        (
            """$map: (\n"""
            """  $bidule: "plop",\n"""
            """    $ping: #000,\n"""
            """);"""
        ),
        [
            ('map', (
                """(\n"""
                """  $bidule: "plop",\n"""
                """    $ping: #000,\n"""
                """)"""
            )),
        ],
    ),
])
def test_valid_blocks(source, attempted):
    """Valid basic variable blocks"""
    parser = ScssVariablesParser()

    result = parser.parse(source)

    assert [item.groups() for item in result] == attempted


@pytest.mark.parametrize("source,attempted", [
    (
        (
            """$white: #ffffff;\n"""
            """$black: #000000;"""
        ),
        [
            ('white', '#ffffff'),
            ('black', '#000000'),
        ],
    ),
    (
        (
            """$white: #ffffff;\n"""
            """// Dummy comment\n"""
            """$empty:;"""
        ),
        [
            ('white', '#ffffff'),
            ('empty', ''),
        ],
    ),
    (
        (
            """$white: #ffffff;\n"""
            """// Dummy comment\n"""
            """$map: (\n"""
            """  $bidule: "plop",\n"""
            """    $ping: #000,\n"""
            """);\n"""
            """$sizes: 1rem 15% 42px;\n"""
        ),
        [
            ('white', '#ffffff'),
            ('map', (
                """(\n"""
                """  $bidule: "plop",\n"""
                """    $ping: #000,\n"""
                """)"""
            )),
            ('sizes', '1rem 15% 42px'),
        ],
    ),
])
def test_multiple_blocks(source, attempted):
    """Multiple variable blocks in source to test parsing on multiline"""
    parser = ScssVariablesParser()

    result = parser.parse(source)

    assert [item.groups() for item in result] == attempted


def test_advanced_settings(settings):
    """Test parsing on an advanced settings files with many variables"""
    sample_path = os.path.join(settings.variables_path, "settings.scss")

    parser = ScssVariablesParser()

    with open(sample_path, 'r') as fp:
        content = fp.read()

    result = parser.parse(content)

    assert [item.groups() for item in result] == [
        ("""emencia-compass-deprecation-warning""", """false"""),
        ("""font-family-opensans""", """"Open Sans", sans-serif"""),
        ("""white""", """#ffffff"""),
        ("""black""", """#000000"""),
        ("""body-font-family""", """$font-family-opensans"""),
        ("""global-font-size""", """16px"""),
        ("""global-weight-normal""", """400"""),
        ("""breakpoint-classes""", """(small medium large xlarge xxlarge)"""),
        ("""small-up""", """screen"""),
        ("""medium-up""", """unquote("screen and #{breakpoint(medium)}")"""),
        ("""sveetoy-breakpoints""", (
            """(\n"""
            """    small: $small-up,\n"""
            """    medium: $medium-up,\n"""
            """)"""
        )),
        ("""sveetoy-smalls""", (
            """(\n    small: 40%,\n    big: 60%,\n)"""
        )),
        ("""sveetoy-underline-thickness""", (
            """(\n"""
            """    thin: (\n"""
            """        size: rem-calc(1px),\n"""
            """        style: solid,\n"""
            """    ),\n"""
            """    normal: (\n"""
            """        size: rem-calc(3px),\n"""
            """        style: solid,\n"""
            """    ),\n"""
            """)"""
        )),
        ("""sveetoy-space-tiny""", (
            """(\n"""
            """    small: 0.5rem,\n"""
            """    medium: 0.75rem,\n"""
            """) !default"""
        )),
        ("""sveetoy-spaces""", (
            """(\n"""
            """    tiny: $sveetoy-space-tiny,\n"""
            """) !default"""
        )),
        ("""button-sml""", """rem-calc(14)"""),
        ("""button-med""", """rem-calc(16)"""),
        ("""sveetoy-button-modests""", (
            """(\n"""
            """    small: $button-sml / 2,\n"""
            """    medium: $button-med / 2,\n"""
            """)"""
        )),
        ("""row-larger-width""", """rem-calc(1328px)"""),
        ("""flex-grid-sizes""", """20 25 33.3333 50 75 100"""),
    ]
