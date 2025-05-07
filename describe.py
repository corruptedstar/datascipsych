import polars as pl
import sys
data_file = sys.argv[1]
data= pl.read_csv (data_file, null_values="n/a")
print (data.describe())
