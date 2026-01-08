from django.shortcuts import render
from .models import CustomUser

def user_list(request):
    return render(request, 'users/user_list.html')
