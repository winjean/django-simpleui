# -*- coding: utf-8 -*-
#  序列化类
from .models import Supplier
from rest_framework import serializers
from .util import get_choices_value


class SupplierSerializer(serializers.ModelSerializer):
    gender_zh = serializers.CharField(read_only=True)
    status_zh = serializers.CharField(read_only=True)

    class Meta:
        model = Supplier

        # 显示全部字段信息
        # fields = '__all__'

        # 显示指定字段信息
        fields = ('name', 'gender', 'gender_zh', 'status', 'status_zh', 'create_time', 'create_user', 'update_time', 'update_user')
