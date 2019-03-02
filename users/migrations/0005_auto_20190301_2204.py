# Generated by Django 2.1.7 on 2019-03-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190228_2255'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Token',
            new_name='UserToken',
        ),
        migrations.AlterModelOptions(
            name='usertoken',
            options={'verbose_name': 'token表', 'verbose_name_plural': 'token表'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'member'), (2, 'vip'), (3, 'svip')], default=1, verbose_name='会员等级'),
        ),
    ]
