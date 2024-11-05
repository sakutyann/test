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

def formworldfunction(request):
          return render(request, 'form.html')

def questformworldfunction(request):
          return render(request, 'questform.html')

def couponformworldfunction(request):
          return render(request, 'coupon.html')

def couponuseformworldfunction(request):
          return render(request, 'couponuse.html')

def couponendformworldfunction(request):
          return render(request, 'couponend.html')


