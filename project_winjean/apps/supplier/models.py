from django.db import models
from .util import get_choices_value


# 各种魔法函数 https://www.zhihu.com/question/46973549/answer/767530541

# Create your models here.
class Supplier(models.Model):
    GENDER_TYPE = (
        (-1, '未知'),
        (0, '女'),
        (1, '男'),
    )

    STATUS_TYPE = (
        (0, '删除'),
        (1, '正常'),
    )

    id = models.CharField(max_length=32, auto_created=True, primary_key=True, verbose_name="主键编号")
    name = models.CharField(max_length=255, unique=True, verbose_name="姓名")
    gender = models.SmallIntegerField(choices=GENDER_TYPE, default=-1, verbose_name="用户性别", help_text="")
    status = models.IntegerField(choices=STATUS_TYPE, default=1, verbose_name="状态")
    create_time = models.DateTimeField(auto_now=False, verbose_name="创建时间")
    create_user = models.CharField(max_length=32, verbose_name="创建用户")
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name="更新时间")
    update_user = models.CharField(max_length=32, null=True, verbose_name="更新用户")

    # 构造方法
    # def __init__(self):
    #     print("调用构造方法")

    @property
    def gender_zh(self):
        return get_choices_value(self.gender, Supplier.GENDER_TYPE)

    @property
    def status_zh(self):
        return get_choices_value(self.status, Supplier.STATUS_TYPE)

    def __str__(self):
        return self.name

    class Meta:
        # 制定生成数据库的表名
        db_table = "t_supplier"
        verbose_name = '供应商信息'
        verbose_name_plural = verbose_name

        # 指定数据库表空间
        # db_tablespace = ''

        # 按哪个字段获取最近的记录
        # get_latest_by = "-update_time"

        # 按订单升序排列 -表示降序 ？表示随机
        ordering = ['create_time', '-update_user']
