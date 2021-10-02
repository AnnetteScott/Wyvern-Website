from django.shortcuts import render

# Create your views here.
def ToWay(request):
  return render(request, 'index.html')