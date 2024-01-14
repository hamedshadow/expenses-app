from django.shortcuts import render
from django.views import View
from expenseswebsite import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
import json


# Create your views here.


# class RegisterationView(View):
#     def get(self, request):
#         # args = {}
#         # args['my_title'] = settings.VARIABLES[1]
#         # args need too pass in below  render command ,args
#         return render(request, 'authentication/register.html',args)


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error':'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'sorry username in use, choose by another one'}, status=409)
        
        return JsonResponse({'username_validate': True})



class RegisterationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')