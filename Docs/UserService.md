# 用户数据类交互定义

1.个人页面设置
前端=>后端（没有特殊说明即为默认值）

{
    user_name: '',
    nickname_of_user: '',
    real_name_of_user: '',
    email: '',
    phone: '',
    credit: '80',
    avator: ''
}

后端=>前端（没有特殊说明即为默认值）

{
    user_name: '',
    nickname_of_user: '',
    real_name_of_user: '',
    email: '',
    phone: '',
    credit: '80',
    avator: ''
}


说明：user_name为用户名，系统生成；
    nickname_of_user为用户昵称，自定义，
    real_name_of_user为用户真实姓名，
    email为用户邮箱，
    phone为用户手机号码，
    credit为用户信誉分，初始为80，
    avator为用户头像，是一个图像


2.修改密码

前端=>后端

{
    new_code:''
}


后端=>前端

{
    old_code:'123456'
}

说明：new_code为用户新设置的密码，默认为123456；
      old_code为用户当前密码

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



