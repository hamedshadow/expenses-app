from django.shortcuts import render
from django.views import View


from expenseswebsite import settings
# Create your views here.


class RegisterationView(View):
    def get(self, request):
        # args = {}
        # args['my_title'] = settings.VARIABLES[1]
        # args need too pass in below  render command ,args
        return render(request, 'authentication/register.html')