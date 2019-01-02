from django.shortcuts import render

# Create your views here.

def card2018(request):
    return render(request, 'holidaycard/card2018.html', {})
    
def card2018wip(request):
    return render(request,'holidaycard/card2018wip.html',{})
