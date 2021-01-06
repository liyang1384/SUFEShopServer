# 订单业务类数据交互定义  
1.我的订单查询  
我的订单列表查询  
前端=>后端（没有特殊说明即为默认值）  
{  
    'user_id': '' //此处user_id不会为空，会传入具体的值  
    'order_type': 0 //0表示买进订单，1表示卖出订单  
    'commodity_name': '',  
    'min_amount': 0,  
    'max_amount': '',
    'order_state': '',  
    'sort': {  
        'name' : 'order_time',  
        'mode' : 'desc' 
    },  
    'page':'1'  
}  
  
说明：commodity_name表示商品名称，min_price和max_price分别表示查询的价格下限和上限（为空字符串时表示没有上限），sort中的name表示排序的字段（只有一个字段参与排序，默认按照下单时间降序排序，即时间晚的在前），mode表示排序方式（asc表示升序，desc表示降序），page表示数据在第几页（每一页最多只需要10条数据，也就是说每次最多只要返回10条数据，默认在第1页）  
  
后端=>前端（仅表示数据格式，具体的值应由查询结果填充）  
[  
    {  
        'commodity_id': '',  
        'commodity_name': '',  
        'commodity_picture': '',  
        'amount': ''  
        'order_time': ''  
        'username': '', //交易对方的用户名  
        'order_state': ''  
    },  
    ... # 最多10条  
]  


2.订单信息查询
后端=>前端（没有特殊说明即为默认值）
{
    order_state: '',
    commodity_picture: '',
    commodity_name: '',
    commodity_type: '',
    price: '',
    payment_platform: '',
    order_time: '2020/12/20',
    payment_time: '2020/12/20', 
    order_id: '',
    seller: '',
    buyer: ''
}

说明：
      order_state表示订单状态;
      commodity_picture表示商品的图像;
      commodity_name表示商品名称；
      commodity_type表示商品类别；
      price表示商品的标价；
      payment_platform表示支付方式；
      order_time表示下单时间；
      payment_time表示付款时间；


3.订单评价（直接作为评价交易对象，假设是卖家的界面，那就把涉及买家的部分屏蔽掉）
前端=>后端（没有特殊说明即为默认值）
{
    score：5，
    comment: '',
    commodity_quality: 5,
    deal_speed: 5,
    seller_attitude: 5,
    order_id,
}

后端=>前端（没有特殊说明即为默认值）
{
    order_state: '',
    commodity_picture: '',
    commodity_name: '',
    commodity_type: '',
    price: '',
    payment_platform: '',
    seller: '',
    buyer: '',
    user_name: '',
    order_id: ''
}

说明：
    order_state表示订单状态
    commodity_picture：商品图像；
    commodity_name表示商品名称；
    commodity_type表示商品类别；
    price表示商品的标价；
    payment_platform表示支付方式；
    seller表示卖家；
    buyer表示买家；
    user_name表示用户名称；
    order_id表示订单ID；
    score表示对买家的综合评分，为数字0-5；
    comment表示用户输入的文字评论；
    commodity_quality表示对于卖家“商品质量”的评价，为数字0-5；
    deal_speed表示对卖家“交易速度”的评价，为数字0-5；
    seller_attitude表示对卖家“卖家态度”的评价，为数字0-5；


4.生成订单
前端=>后端（没有特殊说明即为默认值）  
{  
        'commodity_id': '',
        'user_id': '',
        'amount': ''
}

后端=>前端（仅表示数据格式，具体的值应由查询结果填充）  
[  
    {   
        'order_id': '',
        'commodity_name': '',
        'commodity_type': '', 
        'user_name': '', //卖家的用户名
        'order_time': ''
    }  
]  

5.支付订单(创建payment record)
前端=>后端（没有特殊说明即为默认值）  
{  
        'order_id': '',
        'user_id': '',
        'payment_platform': '',
        'payment_type': '买家付款给平台',
        'order_status': '已付款'
}

后端=>前端（仅表示数据格式，具体的值应由查询结果填充）  
[  
    {   
        'payment_time': '',
        'payment_id': ''
    }  
]  