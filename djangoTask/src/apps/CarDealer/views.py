from rest_framework import viewsets
from .serializers import CarDealerSerializer
from .models import CarDealer
from djangoTask.src.core.tools.permissions import IsCarDealerAdminOrReadOnly


# ---------------View for soft delete from db---------------
class BaseViewSet(viewsets.ModelViewSet):
    def perform_destroy(self, instance, pk=None):
        instance.is_active = False
        instance.save()
# ----------------------------------------------------------


class CarDealerViewSet(BaseViewSet):
    queryset = CarDealer.objects.filter(is_active=True)
    serializer_class = CarDealerSerializer
    permission_classes = (IsCarDealerAdminOrReadOnly,)



