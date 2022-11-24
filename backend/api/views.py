import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse

# JsonResponse, HttpResponse - difference JsonResponse expects dictionary as argument, Http expects string

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first() # to get a random object order_by(?)
    data = {}
    if model_data:
        #data = model_to_dict(model_data) - all fields
        data = model_to_dict(model_data, fields=["id","title","price"]) # declared id title and price to be shown
    return JsonResponse(data)
    #     print(data)
    #     data = dict(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers = {"content-type":"aplication/json"})