'''
Use case:
    * to_csv(df, 'tmp.csv')
    * df = read_csv('tmp.csv')
'''

import pandas as pd


def to_csv(df, path):
    '''Prepend dtypes to the top of df.

    Original source: https://stackoverflow.com/a/50051542/2142093
    source: https://stackoverflow.com/a/54422402/2142093
    '''

    df2 = df.copy()
    df2.loc[-1] = df2.dtypes
    df2.index = df2.index + 1
    df2.sort_index(inplace=True)
    # Then save it to a csv
    df2.to_csv(path, index=False)

def read_csv(path):
    '''Read types first line of csv

    Still doesn't work with datetime64[ns]
    '''

    dtypes = {key:value for (key,value) in pd.read_csv(path,    
              nrows=1).iloc[0].to_dict().items() if 'date' not in value}

    parse_dates = [key for (key,value) in pd.read_csv(path, 
                   nrows=1).iloc[0].to_dict().items() if 'date' in value]
    # Read the rest of the lines with the types from above
    return pd.read_csv(path, dtype=dtypes, parse_dates=parse_dates, skiprows=[1])

