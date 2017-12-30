# -*- coding: utf-8 -*-
import pytest

from boussole.exceptions import InvalidImportRule

def test_ok_001(settings, parser):
    """Single quote"""
    assert parser.strip_quotes("'foo'") == "foo"


def test_ok_002(settings, parser):
    """Double quotes"""
    assert parser.strip_quotes('"foo"') == "foo"


def test_ok_003(settings, parser):
    """Without quotes"""
    assert parser.strip_quotes("foo") == "foo"


def test_error_001(settings, parser):
    """Error, quote starting but not ended"""
    with pytest.raises(InvalidImportRule):
        parser.strip_quotes("'foo")

    with pytest.raises(InvalidImportRule):
        parser.strip_quotes('"foo')


def test_error_002(settings, parser):
    """Error, quote ending but not started"""
    with pytest.raises(InvalidImportRule):
        parser.strip_quotes('foo"')

    with pytest.raises(InvalidImportRule):
        parser.strip_quotes("foo'")
