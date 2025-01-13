from exercises.ex08.data_utils import read_csv_rows, column_values, columnar
from exercises.ex08.DataFrame import DataFrame

""" 1.0 Use read_csv_rows to import both files of data. """
early_data: list[dict[str, str]] = read_csv_rows("data/baby_names_2012_2017.csv")
later_data: list[dict[str, str]] = read_csv_rows("data/baby_names_2018_2021.csv")

""" 1.1 Test column_values function. """
names_early_data: list[str] = column_values(early_data, "name")

""" 1.2 Use columnar to reformat both data sets. """
columnar_early_data: dict[str, list[str]] = columnar(early_data)
columnar_later_data: dict[str, list[str]] = columnar(later_data)

""" 2.0 Create DataFrame objects with each set of data. """
df_early: DataFrame = DataFrame(columnar_early_data)
df_later: DataFrame = DataFrame(columnar_later_data)

""" 2.0 Use tabulate *method* to view data as a table. """
#  df_early.tabulate()  # <- To prevent large output, comment out after testing.

""" 2.1 Use __add__ magic method to combine into one data set. """
df: DataFrame = df_early + df_later
# df.tabulate()  # <- To prevent large output, comment out after testing.

""" 2.2 Use head method to access the first 10 entries of the data frame. """
first_ten: DataFrame = df.head(10)
# first_ten.tabulate()

""" 2.3 Use select method to access only 'name' and 'count' columns. """
name_and_count: DataFrame = df.head(10).select(["name", "count"])
# name_and_count.tabulate()

""" 2.4 Use filter_by_col_value to filter out only people born in 2020. """
names_2020: DataFrame = df.filter_by_col_value("year", "2020")
# names_2020.tabulate()

