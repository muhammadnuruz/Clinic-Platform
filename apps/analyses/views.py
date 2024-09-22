from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from apps.analyses.models import Analyses
from apps.analyses.serializers import AnalysesSerializer


class AnalysesDetailView(RetrieveAPIView):
    serializer_class = AnalysesSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        analyse_id = self.kwargs.get("analyse_id")
        try:
            return Analyses.objects.get(analyse_id=analyse_id)
        except Analyses.DoesNotExist:
            raise NotFound("Analyse with the given id not found")
