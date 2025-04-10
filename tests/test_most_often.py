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

def test_unique_items_one_duplicate():
    example = MostOften(["apple", "banana", "pineapple", "apple", "kiwi", "apple"])
    assert example.get_most_often() == "apple"

def test_unique_items_two_duplicates():
    example = MostOften(["apple", "banana", "pineapple", "apple", "kiwi", "apple", "kiwi", "kiwi"])
    assert example.get_most_often() == "no clear winner"

def test_unique_items_add_item():
    example = MostOften(["apple", "banana", "pineapple", "apple", "kiwi", "apple", "kiwi", "kiwi"])
    example.add_new("apple")
    assert example.get_most_often() == "apple"

def test_unique_items_add_items():
    example = MostOften(["apple", "banana", "pineapple", "apple", "kiwi", "apple", "kiwi", "kiwi"])
    example.add_new("kiwi")
    example.add_new("pineapple")
    example.add_new("pineapple")
    example.add_new("pineapple")
    example.add_new("pineapple")
    assert example.get_most_often() == "pineapple"