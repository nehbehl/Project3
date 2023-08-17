import logging
import pandas as pd


def get_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception:
        logging.info('Error')


def data_cleaning(df):
    try:
        df.columns = df.columns.str.strip()
       
        df['salary'] = df['salary'].str.lstrip()
        df.drop("capital-gain", axis="columns", inplace=True)
        df.drop("capital-loss", axis="columns", inplace=True)
        df.drop("fnlgt", axis="columns", inplace=True)
        df.drop("education-num", axis="columns", inplace=True)
       
        df.to_csv('clean_census.csv')
        return df
    except Exception:
        logging.info('Error')


if __name__ == '__main__':
    df = get_data("census.csv")
    data_cleaning(df)
