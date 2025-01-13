"""Data utility functions."""

__author__ = "720310785"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Function pulls raw data and assigns it to a list of dictionaries consisting of strings."""
    return []


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Function reformats data and produces one row's values as a column."""
    return []


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Function uses the column_values function to reformat ALL data into a format similar to that of a table."""
    return {}
