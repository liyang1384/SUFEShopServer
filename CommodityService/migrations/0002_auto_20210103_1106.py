# Generated by Django 3.1.3 on 2021-01-03 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommodityService', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodityapplication',
            name='application_state',
            field=models.CharField(choices=[('TO_BE_REVIEWED', '待审核'), ('APPROVED', '审核通过'), ('REJECTED', '审核未通过')], default='TO_BE_REVIEWED', max_length=20),
        ),
    ]
