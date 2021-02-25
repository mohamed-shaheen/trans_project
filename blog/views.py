from django.shortcuts import render
from .models import Mobile
# Create your views here.


def home(request):
    mobile_list = Mobile.objects.all()
    context = {'mobile_list' : mobile_list}
    return render(request, 'home.html', context)
