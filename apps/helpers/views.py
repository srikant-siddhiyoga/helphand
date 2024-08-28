from django.shortcuts import render
from rest_framework.views import APIView
from .models import Helpers

class IndexView(APIView):
    def get(self, request):
        helpers = Helpers.objects.all()
        return render(request, 'index.html', {'helpers': helpers})
