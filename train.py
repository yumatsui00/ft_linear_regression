import numpy as np
import pandas as pd
import utils as ft


def training(w0, w1, rate, ite):
    try:
        data = pd.read_csv('data.csv')
        # datacheck
        if not 'km' in data.columns or 'price' not in data.columns or data.empty:
            raise AssertionError("Error: Invalid Format in CSV")
        # remove nan and non digit data
        #data = data[pd.to_numeric(data['km'], errors='coerce').notnull()]  # 'mileage'が数値でない行を削除
        #data = data[pd.to_numeric(data['price'], errors='coerce').notnull()]  # 'price'が数値でない行を削除
        data = data[ft._notnull(ft._to_numeric(data['km'], errors='coerce'))]
        data = data[ft._notnull(ft._to_numeric(data['price'], errors='coerce'))]
        #data['km'] = pd.to_numeric(data['km'])
        #data['price'] = pd.to_numeric(data['price'])
        data = data[(data['km'] >= 0) & (data['price'] >= 0)]
        if data.empty:
            raise AssertionError("Error: There is no valid data in CSV")

        #
        mileages = data['km'].values
        prices = data['price'].values
        #print(mileages)
        #print(prices)

        #学習
        for _ in range(ite):
            price_prediction = w0 + w1 * mileages
            errors = price_prediction - prices
            w0 = w0 - rate * ft._mean(errors)
            w1 = w1 - rate * ft._mean(errors * mileages)
            #print(f"{w0}, {w1}")

            if ft._isnan(w0) or ft._isnan(w1) or ft._isinf(w0) or ft._isinf(w1):
                raise AssertionError("Error: Parameter diverges to inf. Use smaller learning rate")
        return w0, w1


    except FileNotFoundError:
        raise AssertionError("Error: File not Found")
    except AssertionError as e:
        raise e
    except pd.errors.ParserError:
        raise AssertionError("Error: Invalid Format in CSV")
    except PermissionError:
        raise AssertionError("Error: Permission denied")
