from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboard_webpage

urlpatterns = [
    path("", dashboard_webpage),
    path("admin/", admin.site.urls),

    path("dashboard/", dashboard_webpage),
    path("accounts/", include("allauth.urls")),
]
