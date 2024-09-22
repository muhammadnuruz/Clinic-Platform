from django.urls import path

from apps.analyses.views import AnalysesDetailView

urlpatterns = [
    path('<int:analyse_id>/', AnalysesDetailView.as_view(), name='analysis-detail'),
]
