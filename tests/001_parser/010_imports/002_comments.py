# -*- coding: utf-8 -*-
import pytest


def test_remove_005(settings, parser):
    """removing singleline comment case 5"""
    results = parser.remove_comments("""@import "vendor"; //foo""").strip()
    assert results == """@import "vendor";"""


def test_remove_010(settings, parser):
    """trouble with // usage that are not comment"""
    assert parser.remove_comments("""@import url("http://foo.bar/dummy");""") == """@import url("http://foo.bar/dummy");"""


def test_remove_011(settings, parser):
    """trouble with // usage that are not comment"""
    assert parser.remove_comments("""@import url("http://foo.bar/dummy"); // This is a comment""") == """@import url("http://foo.bar/dummy"); """
