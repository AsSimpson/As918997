import pandas as pd
from prettytable import PrettyTable

def format_df(df):    
    table = PrettyTable([''] + list(df.columns))
    for row in df.itertuples():
        table.add_row(row)
    return str(table)

df = pd.read_clipboard(header=None)   # No header provided on example input
print(format_df(df))
