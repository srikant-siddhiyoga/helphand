from django.contrib import admin
from django.urls import path
from apps.helpers.views import HelpersView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helpers/', HelpersView.as_view())
]
