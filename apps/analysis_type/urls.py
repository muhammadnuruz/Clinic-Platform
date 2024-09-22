from django.urls import path

from apps.analysis_type.views import TypesDetailViewSet

urlpatterns = [
    path('search/<str:name>/', TypesDetailViewSet.as_view(),
         name='types-detail'),
]
