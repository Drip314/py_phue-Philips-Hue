from scripts import philip
from django.shortcuts import render


def myview(request):
    lights = request.POST.getlist('lamp')

    if request.POST.get('main') == "toggle":
        philip.on_off(lights)

    if request.POST.get('main') == "apply":
        hue = request.POST.get('hue')
        bri = request.POST.get('bri')
        print(hue)
        print(bri)
        if hue:
            philip.change_color(lights, int(hue))
        if bri:
            philip.change_brightness(lights, int(bri))

    context = {
        'lights': philip.get_lights()
    }

    return render(request, 'index.html', context=context)
