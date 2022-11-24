import json
from django.forms.models import model_to_dict
#from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# JsonResponse, HttpResponse - difference JsonResponse expects dictionary as argument, Http expects string

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"]) # decorator([which metod is allowed]), code bellow Django REST framewoork API view 
def api_home(request, *args, **kwargs):

    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status = 400)
