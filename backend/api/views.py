import json
from django.forms.models import model_to_dict
#from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# JsonResponse, HttpResponse - difference JsonResponse expects dictionary as argument, Http expects string

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["GET"]) # decorator([which metod is allowed]), code bellow Django REST framewoork API view 
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first() # to get a random object order_by(?)
    data = {}
    if instance:
        #data = model_to_dict(instance) - all fields
        data = ProductSerializer(instance).data
        #data = model_to_dict(instance, fields=["id","title","price","sale_price"]) # declared id title and price to be shown
    return Response(data)
    #     print(data)
    #     data = dict(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers = {"content-type":"aplication/json"})