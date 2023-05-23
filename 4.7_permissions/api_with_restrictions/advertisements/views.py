from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements import filters
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    #filter_backends = (DjangoFilterBackend, filters.AdvertisementFilter)
    filterset_fields = ('status', 'created_at', 'updated_at')
    ordering_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    def create(self, request, *args, **kwargs):
        user_profile = request.user.userprofile
        if user_profile.open_ads_count >= 10:
            return Response({'error': 'Max number of open ads reached!'})
        response = super().create(request, *args, **kwargs)
        user_profile.open_ads_count += 1
        user_profile.save()
        return response

    def destroy(self, request, *args, **kwargs):
        ad = self.get_object()
        if ad.author != request.user:
            return Response({'error': 'You can only delete your own ads!'}, status=403)
        response = super().destroy(request, *args, **kwargs)
        request.user.userprofile.open_ads_count -= 1
        request.user.userprofile.save()
        return response

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
