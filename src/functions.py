"""
A list of functions used in the analysis.
"""

import pandas as pd
import datetime as dt


def date_string_to_time(row):
    t = dt.datetime.strptime(row.split('.')[0], '%Y-%m-%d %H:%M:%S')
    return t

def get_cumsum_by(df, by, values):
    df = df.sort_values(by=by)
    cumsum = df[by + values].groupby(by=by).sum().groupby(by=by, level=[0]).cumsum().reset_index()
    df = df.merge(
        right=cumsum,
        how='left',
        on=by,
        suffixes=('', '_cum_sum')
    )
    return df

def get_cumavg_by(df, by, values):
    df = df.sort_values(by=by)
    avg = df[by + values].groupby(by=by).sum().groupby(by=by, level=[0]).mean().reset_index()
    df = df.merge(
        right=avg,
        how='left',
        on=by,
        suffixes=('', '_cum_avg')
    )
    return df




