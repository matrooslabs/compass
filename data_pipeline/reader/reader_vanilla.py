import os
import pyarrow.parquet as pq
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(current_dir)

file_path = os.path.join(parent_dir, 'data/balances/ethereum__balances__18000000_to_18000000.parquet')
# Read the Parquet file
table = pq.read_table(file_path)

# Convert to a pandas DataFrame
df = table.to_pandas()

# Now you can work with the DataFrame as usual
print(df.head())

