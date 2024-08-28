from django.contrib import admin
from django.urls import path
from apps.helpers.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view())
]
