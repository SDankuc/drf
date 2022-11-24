import json
from django.forms.models import model_to_dict
#from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# JsonResponse, HttpResponse - difference JsonResponse expects dictionary as argument, Http expects string

from products.models import Product


@api_view(["GET"]) # decorator([which metod is allowed]), code bellow Django REST framewoork API view 
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first() # to get a random object order_by(?)
    data = {}
    if model_data:
        #data = model_to_dict(model_data) - all fields
        data = model_to_dict(model_data, fields=["id","title","price"]) # declared id title and price to be shown
    return Response(data)
    #     print(data)
    #     data = dict(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers = {"content-type":"aplication/json"})