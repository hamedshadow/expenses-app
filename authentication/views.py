from django.shortcuts import render
from django.views import View
from expenseswebsite import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage,send_mail

# Create your views here.


# class RegisterationView(View):
#     def get(self, request):
#         # args = {}
#         # args['my_title'] = settings.VARIABLES[1]
#         # args need too pass in below  render command ,args
#         return render(request, 'authentication/register.html',args)


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'sorry Email in use, choose by another one'}, status=409)
        
        return JsonResponse({'email_validate': True})


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
    def post(self, request):
        # GET USER DATA
        #VALIDATE
        #CREATE A USER ACCOUNT
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        context = {
            'fieldValue':request.POST
        }
        
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 8:
                    messages.error(request, "password to short")
                    return render(request, 'authentication/register.html',context)
                
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active=False
               
                user.save()
                email_subject='Activate your account'
                email_body = "good to see you and congratuation for createing account"
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [email],
                )
                email.send(fail_silently=False)
                
                messages.success(request, "Account successfuly created")
                return render(request, 'authentication/register.html')
                
                
        return render(request, 'authentication/register.html')

        
        # messages.success(request, 'Success whatsapp success')
        # # messages.warning(request, 'Success whatsapp warning')
        # # messages.info(request, 'Success whatsapp info')
        # # messages.error(request, 'Success whatsapp error')
       
        # return render(request, 'authentication/register.html')