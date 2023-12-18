import pyarrow.parquet as pq
import pandas as pd

# Read the Parquet file
table = pq.read_table('ethereum__balances__18000000_to_18000000.parquet')

# Convert to a pandas DataFrame
df = table.to_pandas()

# Now you can work with the DataFrame as usual
print(df.head())

