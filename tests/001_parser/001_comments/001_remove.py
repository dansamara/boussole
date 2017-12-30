# -*- coding: utf-8 -*-
import pytest

from boussole.parser.comments import ScssCommentsParser


def test_remove_001(settings):
    """removing singleline comment case 1"""
    parser = ScssCommentsParser()
    assert parser.remove_comments("""// foo""") == ""


def test_remove_002(settings):
    """removing singleline comment case 2"""
    parser = ScssCommentsParser()
    assert parser.remove_comments("""//foo
        """).strip() == ""


def test_remove_003(settings):
    """removing singleline comment case 3"""
    parser = ScssCommentsParser()
    assert parser.remove_comments("""
        //foo
    """).strip() == ""


def test_remove_004(settings):
    """removing singleline comment case 4"""
    parser = ScssCommentsParser()
    assert parser.remove_comments("""$foo: true;
// foo
$bar: false;
""").strip() == """$foo: true;\n$bar: false;"""


def test_remove_006(settings):
    """removing multiline comment case 1"""
    parser = ScssCommentsParser()
    assert parser.remove_comments("""/* foo */""") == ""


def test_remove_007(settings):
    """removing multiline comment case 2"""
    parser = ScssCommentsParser()
    assert parser.remove_comments("""
        /*
            * foo
            */""").strip() == ""


def test_remove_008(settings):
    """removing multiline comment case 3"""
    parser = ScssCommentsParser()
    assert parser.remove_comments("""
        /*
            * foo
            */
            $bar: true;""").strip() == "$bar: true;"


def test_remove_009(settings):
    """removing singleline and multiline comments"""
    parser = ScssCommentsParser()
    assert parser.remove_comments("""//Start
/*
 * Pika
 */
$foo: true;
// Boo
$bar: false;
// End""").strip() == "$foo: true;\n$bar: false;"
