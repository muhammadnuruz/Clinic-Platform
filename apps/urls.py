from django.urls import path, include

from apps.view import MessageAPIView

urlpatterns = [
    path('analyses/', include("apps.analyses.urls")),
    path('telegram-users/', include("apps.telegram_users.urls")),
    path('types/', include("apps.analysis_type.urls")),
    path('message/', MessageAPIView.as_view(), name='message-api'),
]
