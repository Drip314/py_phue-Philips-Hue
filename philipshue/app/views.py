from scripts import philip, HexToHue
from django.shortcuts import render


def myview(request):
    lights = request.POST.getlist('lamp')

    if request.POST.get('main') == "toggle":
        philip.on_off(lights)

    if request.POST.get('main') == "apply":
        color = HexToHue.Color(request.POST.get('rgb'))
        bri = request.POST.get('bri')
        print(color)
        print(bri)
        if color:
            philip.change_color(lights, int(color.to_hue()))
        if bri:
            philip.change_brightness(lights, int(bri))

    context = {
        'lights': philip.get_lights()
    }

    return render(request, 'index.html', context=context)
