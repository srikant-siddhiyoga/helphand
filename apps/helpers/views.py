from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import HelpersSerializer
from rest_framework.views import APIView
from rest_framework import status
from .models import Helpers

class HelpersView(APIView):

    def get(self, request):
        helpers = Helpers.objects.all()
        helpers = HelpersSerializer(helpers, many=True).data
        return Response(helpers, status=status.HTTP_200_OK)
    
    def post(self, request):
        helper = HelpersSerializer(data=request.data)
        if helper.is_valid():
            helper.save()
            res = {
                'message': 'Helper created successfully',
                'data': helper.data
            }
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(helper.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        id = request.data.get('id')
        helper = get_object_or_404(Helpers, id=id)
        helper = HelpersSerializer(instance=helper, data=request.data, partial=True)
        if helper.is_valid():
            helper.save()
            res = {
                'message': 'Helper updated successfully',
                'data': helper.data
            }
            return Response(res, status=status.HTTP_200_OK)
        return Response(helper.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        id = request.data.get('id')
        helper = get_object_or_404(Helpers, id=id)
        helper.delete()
        return Response({'message': 'Helper deleted successfully'},status=status.HTTP_204_NO_CONTENT)