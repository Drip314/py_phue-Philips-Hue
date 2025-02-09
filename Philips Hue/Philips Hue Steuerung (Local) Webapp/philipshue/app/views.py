from scripts import philip
from django.shortcuts import render

def myview(request):
    if request.POST.get('main') == "I/O":           
        philip.on_off()        

    print(request.POST.get('main'))
    return render(request, 'index.html')