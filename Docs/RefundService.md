# 退款业务类数据定义

1.退款申请 (以下请求,即为业务顺序步骤)
前端=>后端（让后端知道是哪个用户退款哪个订单）
{
    user_id: '',
    order_id: ''
}

后端=>前端
{
    commidity_picture: '',
    commidity_name: '',
    commidity_type: '',
    price: '',
    amount: '',
    seller: '',
    order_id: '',
    order_time: '',
    payment_time: '',
    payment_platform: ''
}

前端=>后端
{
    user_id: '',
    order_id: '',
    refund_type: '',
    refund_amount: '',（用户实际退款金额）
    refund_reason: '',
    evidence_picture: '',(可能为多张图片，待定)
    refund_time: ''（产生退款申请的时间）
}



2.退款审核  (以下请求,即为业务顺序步骤)
前端=>后端（让后端知道在审核哪个订单）
{
    refund_id: ''
}

后端=>前端
{
    commidity_picture: '',
    commidity_name: '',
    price: '',
    amount: '',
    seller: '',
    buyer: '',
    order_id: '',
    payment_platform: '',
    refund_type: '',
    refund_time: '',
    refund_reason: '',
    evidence_picture: '',
    order_status: ''
}

前端=>后端（告诉后端是否通过退款）
{
    refund_id: '',
    order_status: ''（如果同意，那么就将order_status改成已退款，否则就用原来的
                    order_status)
}

