import sys
import pandas as pd
import numpy as np


# https://github.com/MainakRepositor/Datasets/tree/master/Weather%20Data
# https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Weather%20Data/temperature.csv

def read_data(source):
    return pd.read_csv(source)


def save_data(data, target):
    data.to_csv(target, index=False)


def transform_data(data):
    data = data[['datetime', 'Denver']]
    return data


if __name__ == '__main__':
    print("starting")
    n = len(sys.argv)
    filename = sys.argv[1]
    targetname = sys.argv[2]
    df = read_data(filename)
    df = transform_data(df)
    save_data(df, targetname)
    print("Complete")
