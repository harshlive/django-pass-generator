from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')
def password(request):
    pass_var = ''
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if(request.GET.get('uppercase')):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if(request.GET.get('special')):
        chars.extend(list('!@#$%^&*()'))
    if(request.GET.get('numbers')):
        chars.extend(list('1234567890'))
    len = int(request.GET.get('length'))
    for x in range(len) :
        pass_var +=random.choice(chars)
    return render(request,'generator/password.html',{'password':pass_var})
def about(request):
    return render(request,'generator/about.html')