"""Utility functions."""

__author__ = "730410140"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # close the file when we're done, to free its resources.
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result    


def head(coln_table: dict[str, list[str]], column: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific number of rows."""
    result: dict[str, list[str]] = {}

    for x in coln_table:
        if len(coln_table[x]) < column:
            return coln_table

        list1: list[str] = []
        i = 0
        while i < column:
            list1.append(coln_table[x][i]) 
            i += 1
        result[x] = list1

    return result


def select(table: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original table."""
    result: dict[str, list[str]] = {}

    for x in column:
        result[x] = table[x]
    return result    


def concat(tabu: dict[str, list[str]], tabu2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based tabel with two tables combined."""
    result: dict[str, list[str]] = {} 
    
    for d in tabu:
        result[d] = tabu[d]

    for d in tabu2:
        if d in result:
            result[d] += tabu2[d] 
        else:
            result[d] = tabu2[d]       
    return result