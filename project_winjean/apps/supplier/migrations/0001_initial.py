# Generated by Django 3.2.12 on 2022-04-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=32, primary_key=True, serialize=False, verbose_name='主键编号')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(-1, '未知'), (0, '女'), (1, '男')], default=-1, verbose_name='用户性别')),
                ('status', models.IntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='状态')),
                ('create_time', models.DateTimeField(verbose_name='创建时间')),
                ('create_user', models.CharField(max_length=32, verbose_name='创建用户')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('update_user', models.CharField(max_length=32, null=True, verbose_name='更新用户')),
            ],
            options={
                'verbose_name': '供应商信息',
                'verbose_name_plural': '供应商信息',
                'db_table': 't_supplier',
                'ordering': ['create_time', '-update_user'],
            },
        ),
    ]
