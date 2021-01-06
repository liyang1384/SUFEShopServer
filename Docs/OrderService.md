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
        'user_name': '', //交易对方的用户名  
        'order_state': ''  
    },  
    ... # 最多10条  
]  


2.订单信息查询  (以下请求,即为业务顺序步骤)
前端=>后端（让后端知道是哪个用户，查哪个订单）
{
    order_id: ''
}
后端=>前端（没有特殊说明即为默认值）
{
    commodity_picture: '',
    commodity_name: '',
    commodity_type: '',
    price: '',
    order_state: '',
    order_time: '',
    order_id: '',
    payment_platform: '',
    payment_time: '',
    seller：'',
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


3.订单评价   (以下请求,即为业务顺序步骤)
前端=>后端 (让后端知道哪个用户评价哪个订单)
{
    order_id: '',
    user_id: ''
}

后端=>前端
{
    commidity_picture: '',
    commidity_name: '',
    amount: '',  //实际付款
    commidity_type: '',
    price: '',  //商品金额
    seller: '',
    order_id: '',
    order_time: '',
    payment_platform: '',
    payment_time: ''
}

前端=>后端
{
    order_id: '',
    commodity_quality: '', 
    deal_speed: '',  
    seller_attitude: '',  
    comment: ''
}


4.生成订单
前端=>后端（没有特殊说明即为默认值）  
{  
        'commodity_id': '',
        'seller': '',
        'buyer': '',
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
        'payment_platform': '',
        'payment_type': '买家付款给平台',
        'amount': ''
}

后端=>前端（仅表示数据格式，具体的值应由查询结果填充）  
[  
    {   
        'payment_time': '',
        'payment_id': ''
    }  
]  