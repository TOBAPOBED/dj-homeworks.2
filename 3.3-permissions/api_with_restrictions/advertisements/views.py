from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return []

    def destroy(self, request, *args, **kwargs):
        """Проверка, что пользователь удаляет только своё объявление."""
        instance = self.get_object()
        if instance.creator != request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Вы можете удалять только свои объявления.")
        return super().destroy(request, *args, **kwargs)