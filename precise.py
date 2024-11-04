from train import training
import pandas as pd
import numpy as np
import utils as ft

def check_precision():
    try:
        data = pd.read_csv('data.csv')
        # datacheck
        if not 'km' in data.columns or 'price' not in data.columns:
            raise AssertionError("Error: Invalid Format in CSV")
        data = data[ft._notnull(ft._to_numeric(data['km'], errors='coerce'))]
        data = data[ft._notnull(ft._to_numeric(data['price'], errors='coerce'))]
        data = data[(data['km'] >= 0) & (data['price'] >= 0)]
        if ft._len(data) == 0:
            raise AssertionError("Error: There is no valid data in CSV")

        mileages = data['km'].values
        prices = data['price'].values
        up = []
        down = []
        m = ft._mean(prices)
        w0, w1 = training(0, 0, 0.01, 10000)
        for km, price in zip(mileages, prices):
            predict = w0 + w1 * km
            up.append((price - predict) ** 2)
            down.append((price - m) ** 2)
        r = 1 - ft._sum(up) / ft._sum(down)
        print(f"決定係数R^2 : {r}")

    except FileNotFoundError:
        raise AssertionError("Error: File not Found")
    except AssertionError as e:
        raise e
    except pd.errors.ParserError:
        raise AssertionError("Error: Invalid Format in CSV")
    except PermissionError:
        raise AssertionError("Error: Permission denied")




if __name__ == "__main__":
    check_precision()