import json
from os.path import join

from django.http import JsonResponse
from django.shortcuts import render

from root.settings import BASE_DIR


# Create your views here.
def index_view(request):
    return JsonResponse({"message" : "Salom Dunyo"})


def myme_view(request):
    data = {
        "first_name" : 'Dilshod',
        "last_name" : 'Absaitov',
        "phone_number" : '+998993583231',
        "age" : 24,
    }
    return JsonResponse(data)

def get_param_view(request):
    n1 = request.GET.get('num1')
    n2 = request.GET.get('num2')

    return JsonResponse({"num1" : n1 , 'num2' : n2})

# https://localhost:8000/users
def calculator_view(request):
    n1 = int(request.GET.get('num1'))
    n2 = int(request.GET.get('num2'))
    oper = request.GET.get('oper')

    if oper == "add":
        result = n1 + n2
    elif oper == 'mul':
        result = n1* n2
    elif oper == 'div':
        result = n1/n2
    else:
        result = n1 - n2
    return JsonResponse({'result' : result})


def users_list_view(request):
    with open(join(BASE_DIR, 'apps' ,'files', 'users.json' ) , 'r') as f:
        return JsonResponse(json.load(f))

