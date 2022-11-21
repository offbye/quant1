import tushare as ts
# 初始化pro接口
pro = ts.pro_api('19032df20eca0609a6bab217fb695828507e5683d2d1cbd3e31b9ccc')

# 拉取数据
df = pro.fund_basic(**{
    "ts_code": "",
    "market": "",
    "update_flag": "",
    "offset": "",
    "limit": "",
    "status": "",
    "name": ""
}, fields=[
    "ts_code",
    "name",
    "management",
    "custodian",
    "fund_type",
    "found_date",
    "due_date",
    "list_date",
    "issue_date",
    "delist_date",
    "issue_amount",
    "m_fee",
    "c_fee",
    "duration_year",
    "p_value",
    "min_amount",
    "exp_return",
    "benchmark",
    "status",
    "invest_type",
    "type",
    "trustee",
    "purc_startdate",
    "redm_startdate",
    "market"
])
print(df)
df.to_csv('jijin.csv')