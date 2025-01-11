import pandas as pd
# read csv
df = pd.read_csv('data/player_data.csv', header=0,delim_whitespace=True)
df.drop('Awards', axis=1, inplace=True)
# parsing function by position
def pgCsv(dataframe):
    value = "PG"
    df2 = dataframe.loc[dataframe["Pos"] == value].copy()
    df2.to_csv('data/pg_data.csv',sep=' ', index=False)

def centerCsv(dataframe):
    value = "C"
    df2 = dataframe.loc[dataframe["Pos"] == value].copy()
    df2.to_csv('data/enter_.csv',sep=' ', index=False, )
def sgCsv(dataframe):
    value = "SG"
    df2 = dataframe.loc[dataframe["Pos"] == value].copy()
    df2.to_csv('data/sg_data.csv',sep=' ', index=False)
def sfCsv(dataframe):
    value = "SF"
    df2 = dataframe.loc[dataframe["Pos"] == value].copy()
    df2.to_csv('data/sf_data.csv', sep=' ',index=False)
def pfCsv(dataframe):
    value = "PF"
    df2 = dataframe.loc[dataframe["Pos"] == value].copy()
    df2.to_csv('data/pf_data.csv', sep=' ',index=False)
#calls to each function 
pgCsv(df)
centerCsv(df)
sgCsv(df)
pfCsv(df)
sfCsv(df)






    