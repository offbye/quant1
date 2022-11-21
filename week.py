import tushare as ts
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 2)
# 初始化pro接口
pro = ts.pro_api('19032df20eca0609a6bab217fb695828507e5683d2d1cbd3e31b9ccc')

# 拉取数据
df = pro.weekly(**{
    "ts_code": "002241.SZ",
    "trade_date": "",
    "start_date": "20191011",
    "end_date": "20221118",
    "limit": 1000,
    "offset": ""
}, fields=[
    "ts_code",
    "trade_date",
    "close",
    "open",
    "high",
    "low",
    "pre_close",
    "change",
    "pct_chg",
    "vol",
    "amount"
])
print(df)
