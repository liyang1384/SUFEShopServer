# 用户数据类交互定义

1.个人页面设置  (以下请求,即为业务顺序步骤)
前端=>后端（让后端知道要查询的是哪个人）
{
    user_id: ''
}

后端=>前端（后端得到user_id后，把user的信息发送给前端）
{
    user_name: '',
    nick_name: '',
    email: '',
    mobile: '',
    credit: '',  （信誉分）
    avator: '', （头像）

}

前端=>后端（前端得到新的用户上传的用户信息，上传给后端）
{
    user_name: '',
    nick_name: '',
    email: '',
    mobile: '',
    credit: '',  （信誉分）
    portrait: '', （头像）

}


说明：user_id为用户名，系统生成；
    nick_name为用户昵称，自定义，
    user_name为用户真实姓名，
    email为用户邮箱，
    mobile为用户手机号码，
    credit为用户信誉分，初始为80，
    avator为用户头像，是一个图像


2.修改密码 (以下请求,即为业务顺序步骤)

前端=>后端（用户输入新密码，旧密码，前端将以下信息发送给后端验证）

{
    user_id: '',
    password: '',
    new_password: ''
}


后端=>前端（密码验证由后端负责，如果正确，返回flag=True，否则为False）

{
    flag: false
}


3.注册  
前端=>后端  
{
    'user_name':'', // 非默认值
    'password':'', // 非默认值
    'email':'', // 非默认值
    'real_name':'', // 非默认值
    'mobile':'' // 非默认值
}

后端=>前端
{
    'status_code' = 200 // 注册成功是200，其他失败情况请自定义（如用户名已被占用）
}

4.登录
前端=>后端
{
    'user_name':'', // 非默认值
    'password':'', // 非默认值
    
}
后端=>前端
{
    'status_code' = 200 // 登录成功是200，账号密码错误是401，被禁用是403
}



