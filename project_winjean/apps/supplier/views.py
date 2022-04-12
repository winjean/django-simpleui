import logging

from rest_framework.viewsets import ModelViewSet
from .models import Supplier
from .serializers import SupplierSerializer
from django.http import JsonResponse


logger = logging.getLogger(__name__)


def printTableField(request):
    for f in Supplier._meta.fields:
        print(f.name, f.verbose_name)

    arr = [{"a": "a", "b": "b"}, {"c": "c", "d": "d"}]
    return JsonResponse(arr, safe=False)


class SupplierSet(ModelViewSet):

    # 模型表需要拿出所有数据，内部会自动进行增删改查
    # order_by 先于 models中ordering排序 -create_time 为按创建时间逆序
    queryset = Supplier.objects.all().order_by('-update_time')

    # 序列化后会自动进行返回数据
    serializer_class = SupplierSerializer

    def create(self, request, *args, **kwargs):
        print("self create")
        logger.error(" ... create self ...")

        return ModelViewSet.create(self, request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print("self retrieve")
        logger.error(" ... retrieve self ...")

        return ModelViewSet.retrieve(self, request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        print("self update")
        logger.error(" ... update self ...")

        return ModelViewSet.update(self, request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        print("self partial_update")
        logger.error(" ... partial_update self ...")

        return ModelViewSet.partial_update(self, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        print("self destroy")
        logger.error(" ... destroy self ...")

        return ModelViewSet.destroy(self, request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        print("self list")
        logger.info(" ... list self info ...")
        logger.debug(" ... list self debug ...")
        logger.error(" ... list self error ...")
        return ModelViewSet.list(self, request, *args, **kwargs)
