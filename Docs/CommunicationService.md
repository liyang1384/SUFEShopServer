# 消息业务类数据交互定义  
1.发送消息
前端=>后端  
{  
    'user': '',
    'receive_user': '',  
    'message_content': '' 
}  

后端=>前端（仅表示数据格式，具体的值应由查询结果填充）  
[  
    {  
    },  
]  

2.接收所有消息
前端=>后端  
{  
    'receive_user': ''
}  

后端=>前端（仅表示数据格式，具体的值应由查询结果填充）  
[  
    {  
        'user': '',
        'online_state':'',
        'message_content': '' 
        'send_time': '',
        'avatar':''
    }
] 
说明：user指的是这条消息的发送者，不仅要给我发每条消息的发送者，也要把发送者当前的在线情况发过来，就是online_state，以及发送者的头像。