# Generated by Django 3.1.3 on 2020-12-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserService', '0002_auto_20201207_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='new_user', max_length=30),
        ),
    ]