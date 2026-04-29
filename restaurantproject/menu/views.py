from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the restaurant menu!")


def menu_list(request):
    return HttpResponse("Menu items will be displayed here.")

def item_details(request,item_id):
    """ show details of the speicific item !!"""
    return HttpResponse(f"Details of items {item_id}")

def about(request):
    """About the page """
    return HttpResponse("About : We serve the great food")

def menu_json(request):
    """API end point - Return Json"""
    data = {"items":["Pasta","Salmon","Salad"]}
    return JsonResponse(data)

