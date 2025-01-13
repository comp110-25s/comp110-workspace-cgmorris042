from __future__ import annotations
from tabulate import tabulate  # type: ignore (this just suppresses the warning.)


class DataFrame:

    data: dict[str, list[str]]

    def __init__(self, data: dict[str, list[str]]):
        return None

    def tabulate(self) -> None:
        print(tabulate(self.data, headers=list(self.data.keys()), tablefmt="grid"))

    def head(self, rows: int) -> DataFrame:
        return DataFrame({})

    def __add__(self, other: DataFrame) -> DataFrame:
        return DataFrame({})

    def select(self, selected_columns: list[str]) -> DataFrame:
        return DataFrame({})

    def filter_by_col_value(self, column_name: str, col_value: str) -> DataFrame:
        return DataFrame({})

    