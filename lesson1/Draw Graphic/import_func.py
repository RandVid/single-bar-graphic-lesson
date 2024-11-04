import pandas as pd


def import_dataset():
    df = pd.read_csv('dataset.csv')
    df = df[df['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]
    df.sort_values(by='genre', inplace=True)
    return df

