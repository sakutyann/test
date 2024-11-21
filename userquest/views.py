from django.shortcuts import render

def questnowformworldfunction(request):
          return render(request, 'questnow.html')

def questnotformworldfunction(request):
          return render(request, 'questnot.html')

def questdoformworldfunction(request):
          return render(request, 'questdo.html')

def questgoformworldfunction(request):
          return render(request, 'questgo.html')

def questyesformworldfunction(request):
          return render(request, 'questyes.html')

def questoutformworldfunction(request):
          return render(request, 'questout.html')


def questfinformworldfunction(request):
          return render(request, 'questfin.html')

# Create your views here.
