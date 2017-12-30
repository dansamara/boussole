# -*- coding: utf-8 -*-
"""
Comments
========

This parser is in charge to find every comments in given Sass content.
"""
from __future__ import unicode_literals

import re


class ScssCommentsParser(object):
    """
    SCSS parser to find comments.

    Commonly it is used to remove comment before parsing for other feature and
    avoid false positive.

    Attributes:
        REGEX_COMMENTS: Compiled regex used to find comments.
    """
    # Second part (for singleline comment) contain a negative lookbehind
    # assertion to avoid to match on url protocole (http://) and cause issues
    # in parsing
    REGEX_COMMENTS = re.compile(r'(/\*.*?\*/)|((?<!(:))//.*?(\n|$))',
                                re.IGNORECASE | re.DOTALL)

    def remove_comments(self, content):
        """
        Remove all comment kind (inline and multiline) from given content.

        Args:
            content (str): A SCSS source.

        Returns:
            string: Given SCSS source with all comments removed.
        """
        return self.REGEX_COMMENTS.sub("", content)
