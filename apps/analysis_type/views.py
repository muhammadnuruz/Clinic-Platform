from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django.db.models import Q
from rest_framework.exceptions import NotFound
from apps.analysis_type.models import Types
from apps.analysis_type.serializers import TypesSerializer

class TypesDetailViewSet(ListAPIView):
    serializer_class = TypesSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Types.objects.all()
        name = self.kwargs.get('name')
        if name:
            queryset = queryset.filter(Q(name__icontains=name) | Q(ru_name__icontains=name))
        if not queryset.exists():
            raise NotFound("Type with the given criteria not found")
        return queryset
