from django.shortcuts import render,redirect
from django.views import View
from expenseswebsite import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage,send_mail
from django.contrib import auth
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
import django.utils.encoding
from django.urls import reverse
from .utils import token_generator
from django.core.mail import EmailMessage



account_activation_token = token_generator

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
                #path_to_view
                # - getting domain we are on
                # - relative url to verification
                # - encode uid 
                # - get token
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                link = reverse('activate', kwargs={'uidb64':uidb64,'token': token_generator.make_token(user)})
                activate_url = 'http://' + domain + link 
                email_subject='Activate your account'
                email_body = "Hi " + user.username + " please use this link to verify your account\n" + activate_url
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semycolon.com',
                    [email],
                )
                email.send(fail_silently=False)
                

                user.is_active = False
                user.save()
                email_subject = "Ativation your account"
                email_body = "hello dear you can useing your dashboard now"
                email = EmailMessage(
                    [email_subject],
                    [email_body],
                    [email],
                )
                email.send(fail_silently=False)

                messages.success(request, "Account successfuly created")
                return render(request, 'authentication/register.html')
                
                
        return render(request, 'authentication/register.html')


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            if not account_activation_token.check_token(user,token):
                return redirect('login'+ '?message= '+ 'User already activate')
            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()
            messages.success(request,'Account activated successfully')
            return redirect('login')
        except Exception as ex:
            pass
        
        return redirect('login')
    

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')









        
        # messages.success(request, 'Success whatsapp success')
        # # messages.warning(request, 'Success whatsapp warning')
        # # messages.info(request, 'Success whatsapp info')
        # # messages.error(request, 'Success whatsapp error')
       
        # return render(request, 'authentication/register.html')