from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

def about(request):
    """ """
    return JsonResponse({"Detail":"This is about page of the app - app"})

# Create your views here.
PRODUCT_CATALOG = {
    "SKU456": {"sku": "SKU456", "name": "Mechanical Keyboard", "price": 89.5, "currency": "USD"},
    "DEF456": {"sku": "DEF456", "name": "Truffle Pasta",    "price": 18.50, "currency": "USD"},
    "GHI789": {"sku": "GHI789", "name": "Caesar Salad",     "price": 9.75,  "currency": "USD"},
}

def product_detail_view(request,sku):
    if request.method != 'GET':
        return JsonResponse({"detail":"Mehtod not allowed"},status=405)
    
    product = PRODUCT_CATALOG.get(sku)
    if product is None :
        return JsonResponse({"detail":"Not Found"},status=404)
    
    else :
        return JsonResponse(product)


def welcome_view(request,name):
    if request.method != 'GET':
        response = HttpResponse("method not allwoed", status = 405,content_type = 'text/plain')
        response["Allow"] = "GET"
        return response

    return HttpResponse(f"Welcome to Django. {name}!",content_type='text/plain') 

class GreetView(View):
    http_method_names = ['get']

    def get(self,request,username):
        message = f"Hello , {username}"
        return HttpResponse(message)
