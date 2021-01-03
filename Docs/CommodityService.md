# 商品业务类数据交互定义
1.商品审核
商品审核列表查询
前端=>后端
{
    'application_state': 'TO_BE_REVIEWED'
    'commodity_name': '',
    'min_price': 0,
    'max_price': '',
    'sort': {
        'name' : 'apply_time',
        'mode' : 'asc'
    },
    'username': '',
    'auditor_name': '',
    'page':'1'
}

说明：application_state表示审核状态，commodity_name表示商品名称（如果非空，只要包括即视为符合条件,username和auditor_name也这样），min_price和max_price分别表示查询的价格下限和上限（为空字符串时表示没有上限），sort中的name表示排序的字段（只有一个字段参与排序，默认按照申请时间升序排序，即时间早的在前），mode表示排序方式（asc表示升序，desc表示降序），page表示数据在第几页（每一页最多只需要10条数据，也就是说每次最多只要返回10条数据，默认在第1页），username表示申请人用户名，auditor_name表示审核员用户名

后端=>前端（仅表示数据格式，具体的值应由查询结果填充）
[
    {
        'commodity_id': '',
        'commodity_name': '',
        'price': ''
        'apply_time': ''
        'username': '',
        'auditor_name': '',
        'audit_time': '',
    },
    ... # 最多10条
]
当application_state为未审核时，auditor和auditor_time字段值应为''

