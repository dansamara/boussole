# -*- coding: utf-8 -*-
"""
Variables
=========

This parser is in charge to find every variables rules in given Sass content.
"""
from __future__ import unicode_literals

import re


class ScssVariablesParser(object):
    """
    SCSS parser to find variables rules.
    """
    REGEX_VARIABLE_BLOCK = re.compile(r"(?P<selector>\$[\w\-]+)\s*:\s*(?P<properties>[^;]*?)\s*\;")

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
        Parse a stylesheet document with a regex

        Args:
            content (str): A SCSS source.

        Returns:
            list: Finded variables
        """
        return self.find_variable_blocks(content)
