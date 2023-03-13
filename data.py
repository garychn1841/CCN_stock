import pandas as pd
import talib as ta

df = pd.read_csv('/Users/gary/Documents/Python/CCN_stock/dataset/2330.csv')
print(df.drop(['證券代碼','簡稱'],axis=1))

ma = ta.SMA(df['收盤價(元)'],6)
print(ma)