from django.shortcuts import render
import os
import json 
from django.conf import settings

# Create your views here.


def index(request):
    currency_data = []
    file_path= os.path.join(settings.BASE_DIR, 'currencies.json') 
    import pdb
    pdb.set_trace()
    return render(request,'preferences/index.html')