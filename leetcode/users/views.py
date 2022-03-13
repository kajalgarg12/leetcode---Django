from django.shortcuts import render
from django.http import JsonResponse

def login(request):
    return JsonResponse(data={'msg':"data"})
