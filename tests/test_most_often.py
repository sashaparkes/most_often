from lib.most_often import *
import pytest

def test_empty_list():
    example = MostOften([])
    assert example.starting_list == []

def test_add_new():
    example = MostOften([])
    example.add_new("apple")
    assert example.starting_list == ["apple"]

def test_add_another_item():
    example = MostOften(["banana"])
    example.add_new("apple")
    assert example.starting_list == ["banana", "apple"]

def test_unique_items_one_item():
    example = MostOften(["banana"])
    assert example.get_most_often() == "banana"

def test_unique_items_draw():
    example = MostOften(["banana", "apple"])
    assert example.get_most_often() == "no clear winner"

def test_unique_items_empty_list():
    example = MostOften([])
    assert example.get_most_often() == "no clear winner"
