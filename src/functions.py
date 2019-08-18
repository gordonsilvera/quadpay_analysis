"""
A list of functions used in the analysis.
"""

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
