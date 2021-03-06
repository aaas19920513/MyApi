# Generated by Django 2.1.7 on 2019-07-07 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('begin', '0012_remove_case_config'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='名称')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='begin.Classify', verbose_name='父类目')),
            ],
            options={
                'verbose_name': '接口分类',
                'verbose_name_plural': '接口分类',
                'db_table': 'classify',
            },
        ),
    ]
