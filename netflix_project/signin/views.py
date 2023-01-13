from django.shortcuts import render

# Create your views here.

def signin(request):
    return render(request,'signin_templates/signin.html')


def signup(request):
    return render(request,'signin_templates/signup_page.html')