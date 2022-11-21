import tushare as ts
# 初始化pro接口
pro = ts.pro_api('19032df20eca0609a6bab217fb695828507e5683d2d1cbd3e31b9ccc')

# 拉取数据
df = pro.stock_basic(**{
    "ts_code": "",
    "name": "",
    "exchange": "",
    "market": "",
    "is_hs": "",
    "list_status": "",
    "limit": 8000,
    "offset": ""
}, fields=[
    "ts_code",
    "symbol",
    "name",
    "area",
    "industry",
    "market",
    "list_date"
])
print(df)
df.to_csv("stocks2.csv")