# Generated by Django 3.1.3 on 2021-01-03 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderService', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerreview',
            name='if_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='if_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='paymentrecord',
            name='if_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sellerreview',
            name='if_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='buyerreview',
            name='review_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='评价时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_state',
            field=models.CharField(choices=[('paying', '待付款'), ('paid', '已付款'), ('refunded', '已退款'), ('cancelled', '已取消')], default='待付款', max_length=30, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='下单时间'),
        ),
        migrations.AlterField(
            model_name='paymentrecord',
            name='payment_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='支付时间'),
        ),
        migrations.AlterField(
            model_name='sellerreview',
            name='review_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='评价时间'),
        ),
    ]
