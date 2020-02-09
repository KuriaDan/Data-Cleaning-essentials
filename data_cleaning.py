import pandas as pd
def initial_eda_checks(df):
    """Takes a dataframe and prints out the percentage of the dataframe that is missing"""
    if df.isnull().sum().sum() > 0:
        mask_total = df.isnull().sum().sort_values(ascending=False)
        total = mask_total[mask_total > 0]
        mask_percent = df.isnull().mean().sort_values(ascending=False)
        percent = mask_percent[mask_percent > 0]
        missing_data=pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
        print(f'Total and percentage NaN\n {missing_data}')
    else:
        print('No NaN found')

def view_column_w_many_nans(df, missing_percent):
    mask_percent = df.isnull().mean()
    series=mask_percent[mask_percent > missing_percent]
    columns = series.index.tolist()
    print(columns)
    return columns
def drop_columns_w_many_nans(df, missing_percent):
    series = view_column_w_many_nans(df, missing_percent=missing_percent)
    list_of_cols = series
    df.drop(columns=list_of_cols, inplace=True)
    print(list_of_cols)
def cleaning_column_names(df):
    df.columns=df.columns.str.lower().str.replace(' ', '_')
    return df