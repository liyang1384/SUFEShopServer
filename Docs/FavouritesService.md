# 收藏夹业务类数据交互定义  
1.将指定商品添加到收藏夹
前端=>后端（没有特殊说明即为默认值）  
{  
        'commodity_id': '',
        'user_id': ''
}

后端=>前端（仅表示数据格式，具体的值应由查询结果填充）  
[  
    {   
        'commodity_name': '',  
        'commodity_picture': '',
        'commodity_type': '', 
        'collect_time': ''  
        'user_name': '', //卖家的用户名  
        'commodity_state': '',
        'price':''
    }  
]  

2.获取个人收藏夹信息
前端=>后端（没有特殊说明即为默认值）  
{  
    'user_id': '' //此处user_id不会为空，会传入具体的值
    'commodity_name': '', 
    'min_amount': 0,  
    'max_amount': '',
    'commodity_state': '',  
    'sort': {  
        'name' : 'collect_time',  
        'mode' : 'desc' 
    },  
    'page':'1'  
}  
  
说明：commodity_name表示商品名称，sort中的name表示排序的字段（只有一个字段参与排序，默认按照下单时间降序排序，即时间晚的在前），mode表示排序方式（asc表示升序，desc表示降序），page表示数据在第几页（每一页最多只需要10条数据，也就是说每次最多只要返回10条数据，默认在第1页）  
  
后端=>前端（仅表示数据格式，具体的值应由查询结果填充）  
[  
    {   
        'commodity_id': '',
        'commodity_name': '',  
        'commodity_picture': '',
        'commodity_type': '',   
        'amount': ''  
        'collect_time': ''  
        'user_name': '', //卖家的用户名  
        'commodity_state': '',
        'price':''
    },  
    ... # 最多10条  
]  


3.删除收藏夹中的商品
前端=>后端（没有特殊说明即为默认值）  
{  
        'commodity_id': '',
        'user_id': ''
}

后端=>前端（仅表示数据格式，具体的值应由查询结果填充）  
[  
    {   
        'commodity_name': '',  
        'commodity_picture': '',
        'commodity_type': '', 
        'user_name': '', //卖家的用户名  
        'commodity_state': '',
        'price':''
    }  
] 