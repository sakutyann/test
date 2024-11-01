from django.shortcuts import render

# Create your views here.

def loginworldfunction(request):
          return render(request, 'login.html')

def mainworldfunction(request):
          return render(request, 'main.html')

def accountworldfunction(request):
          return render(request, 'account.html')

def logoutworldfunction(request):
          return render(request, 'logout.html')