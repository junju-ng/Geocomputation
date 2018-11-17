import pandas as pd
import os

cwd = os.getcwd()
data_dir = cwd + '/data'

dir_list = next(os.walk(data_dir))[1]

COL_dfs = []
street_dfs = []
COL_sns_dfs = []
metro_street_dfs = []


for month in dir_list:
    month_path = os.path.join(data_dir, month)
    COL_outcomes = os.path.join(month_path, month + '-city-of-london-outcomes.csv')
    COL_crime = os.path.join(month_path, month + '-city-of-london-street.csv')
    COL_sns = os.path.join(month_path, month + '-city-of-london-stop-and-search.csv')
    metro_street = os.path.join(month_path, month + '-metropolitan-street.csv')

    COL_df = pd.read_csv(COL_outcomes, engine='python')
    street_df = pd.read_csv(COL_crime, engine='python')
    COL_sns_df = pd.read_csv(COL_sns, engine='python')
    metro_street_df = pd.read_csv(metro_street, engine='python')

    COL_dfs.append(COL_df)
    street_dfs.append(street_df)
    COL_sns_dfs.append(COL_sns_df)
    metro_street_dfs.append(metro_street_df)

full_COL_dfs = pd.concat(COL_dfs)
full_COL_dfs.to_csv('COL_outcomes.csv', sep='\t')

full_street_dfs = pd.concat(street_dfs)
full_street_dfs.to_csv('COL_street.csv', sep='\t')

full_sns_dfs = pd.concat(COL_sns_dfs)
full_sns_dfs.to_csv('COL_sns.csv', sep='\t')

full_metro_street_dfs = pd.concat(metro_street_dfs)
full_metro_street_dfs.to_csv('metro_street.csv', sep='\t')




