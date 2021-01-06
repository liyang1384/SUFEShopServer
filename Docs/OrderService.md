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
    status_of_order: '',
    Image: '',
    name_of_commidity: '',
    class_of_commidity: '',
    price_of_commidity: '',
    real_price_of_commidity: '',
    method_of_pay: '',
    time_of_deal: '2020/12/20',
    time_of_pay: '2020/12/20',
    time_of_delivery: '2020/12/20',
    time_of_receive: '2020/12/20',
    no_of_order: '',
    seller: '',
    buyer: ''
}

说明：
      status_of_order表示订单状态，0和1表示退单和未退单
      Image表示商品的图像;
      name_of_commidity表示商品名称；
      class_of_commidity表示商品类别；
      price_of_commidity表示商品的标价；
      real_price_of_commidity表示商品的实际付价；
      method_of_pay表示支付方式；
      time_of_deal表示下单时间；
      time_of_pay表示付款时间；
      time_of_delivery表示发货时间；
      time_of_receive表示收货时间


3.订单评价（直接作为评价交易对象，假设是卖家的界面，那就把涉及买家的部分屏蔽掉）
前端=>后端（没有特殊说明即为默认值）
{
    review: '',
    description: 5,
    speed: 5,
    attitude: 5,
    fileList: []
}

后端=>前端（没有特殊说明即为默认值）
{
    status_of_order表示订单状态，0和1表示退单和未退单
    status_of_order: '',
    Image: '',
    name_of_commidity: '',
    class_of_commidity: '',
    price_of_commidity: '',
    real_price_of_commidity: '',
    method_of_pay: '',
    seller: '',
    buyer: '',
    user_name: '',
    no_of_order: ''
}

说明：
    Image：商品图像；
    user_name: '用户名称',
    name_of_commidity表示商品名称；
    class_of_commidity表示商品类别；
    price_of_commidity表示商品的标价；
    real_price_of_commidity表示商品的实际付价；
    method_of_pay表示支付方式；
    seller表示卖家；
    review表示用户输入的评论；
    description表示用户对于“描述与事实相符”的评价，为数字0-5；
    speed表示用户对“发货速度”的评价，为数字0-5；
    attitude表示用户对“卖家态度”的评价，为数字0-5；
    filelist为用户上传的一组图片，作为评价的凭证；


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