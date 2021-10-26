"""Some helpful utility functions for working with csv files."""

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into a "table' """
    result: list[dict[str, str]] = []
    #To do: More work!

    file_handle = open(filename, "r", encoding='utf8')
    #Prepare to read the data file as a CSV rather tahn just strings
    csv_reader = DictReader(file_handle)
    
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)


    #Close the file when we are done to free it's resources.
    file_handle.close()

    return result 



def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """produce a list[str]  of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to aa column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)

    return result