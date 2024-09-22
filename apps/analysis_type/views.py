from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.db.models import Q
from rest_framework.exceptions import NotFound
from apps.analysis_type.models import Types
from apps.analysis_type.serializers import TypesSerializer

class TypesDetailViewSet(RetrieveAPIView):
    serializer_class = TypesSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Types.objects.all()
        name = self.kwargs.get('name')  # Use path parameter
        if name:
            queryset = queryset.filter(Q(name__icontains=name) | Q(ru_name__icontains=name))
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        if queryset.exists():
            return queryset.first()
        else:
            raise NotFound("Type with the given criteria not found")
