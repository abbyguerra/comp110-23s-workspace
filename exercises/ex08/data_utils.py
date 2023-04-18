"""Dictionary related utility functions."""


__author___ = 730556346


from csv import DictReader 


def read_csv_rows(path: str) -> list[dict[str, str]]: 
    """Reading the csv file row by row."""
    output: list[dict[str, str]] = []

    file_reader = open(path, "r", encoding = "utf8")

    csv_reader = DictReader(file_reader)

    for row in csv_reader: 
        output.append(row)

    file_reader.close()


def column_values(table: list[dict[str,str]], column_name: str) -> list[str]: 
    """Producing a list of all values in a single column whose name is the second parameter."""
    output: list[str] = []
    for row in table: 
        value: str = row[column_name]
        output.append(value)

    return output


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Making a row oriented table a column oriented table."""
    output: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for columm in first_row: 
        output[column] = column_values(row_table, column)

    return output 


def head(dict1: dict[str, list[str]], length: int) -> dict[str, list[str]]: 
    """Makes a new table with first N."""
    if len(dict1) < length: 
        length = len(dict1)
    result: dict[str, list[str]] = {}
    for column in dict1: 
        something: list[str] = []
        i: int = 0
        while i < length: 
            something.append(dict1[column][i])
            i += 1

        result[column] = something 
    
    return result


def select(a: dict[str, list[str]], b: list[str]) -> dict[str, list[str]]: 
    """Produce a column with a specific subset."""
    empty: dict[str, list[str]] = {}
    for x in a: 
        if x in b: 
            empty[x] = a[x]

    return empty 


def concat(C: dict[str, list[str]], D: dict[str, list[str]]) -> dict[str, list[str]]: 
    """Two column based tables combined."""
    empty2: dict[str, list[str]] = {}
    for x in C: 
        empty2[x] = C[x]
        for y in D: 
            if y in C: 
                empty2[y] = C[y] + D[y]
            else: 
                empty2[y] = D[y]

    return empty2


def count(e: list[str]) -> dict[str, int]:
    """Produce unique values in the list."""
    result: dict[str, int] = {}
    for x in e: 
        if x in result: 
            result[x] += 1
        else: 
            result[x] = 1
    
    return result

                 