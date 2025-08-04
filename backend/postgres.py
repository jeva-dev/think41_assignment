import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:6369Brutal!@localhost:think41')
df = pd.read_csv('mypath.csv')
df.to_sql("my_table_name", engine)   