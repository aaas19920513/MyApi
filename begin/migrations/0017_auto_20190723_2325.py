# Generated by Django 2.1.7 on 2019-07-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('begin', '0016_auto_20190723_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='protocol',
            field=models.CharField(default='http', max_length=10, verbose_name='请求协议'),
        ),
    ]