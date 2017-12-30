# -*- coding: utf-8 -*-
"""
Variables parser
================

This parser is in charge to find every variables rules in given Sass content.
"""
from __future__ import unicode_literals

import re

from boussole.parser.comments import ScssCommentsParser


class ScssVariablesParser(ScssCommentsParser):
    """
    SCSS parser to find variables rules.

    Attributes:
        REGEX_VARIABLE_BLOCK: Compiled regex used to match variables blocks.
        Every match contain ``selector`` and ``properties`` groups.
    """
    REGEX_VARIABLE_BLOCK = re.compile(r"\$(?P<selector>[\w\-]+)\s*:\s*(?P<properties>[^;]*?)\s*\;")

    def find_variable_blocks(self, content):
        """
        Use regex ``REGEX_VARIABLE_BLOCK`` to find every variable blocks from
        given content

        Args:
            content (str): A SCSS source.

        Returns:
            list: List of matched groups for every block
        """
        return self.REGEX_VARIABLE_BLOCK.finditer(content)

    def parse(self, content):
        """
        Parse a stylesheet document for every variables

        Args:
            content (str): A SCSS source.

        Returns:
            list: Finded variables
        """
        cleaned = self.remove_comments(content)

        return self.find_variable_blocks(cleaned)
