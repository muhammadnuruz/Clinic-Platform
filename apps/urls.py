from django.urls import path, include

urlpatterns = [
    path('analyses/', include("apps.analyses.urls")),
    path('telegram-users/', include("apps.telegram_users.urls")),
    path('types/', include("apps.analysis_type.urls")),
]
