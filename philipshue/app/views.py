from scripts import philip, HexToHue
from django.shortcuts import render


def myview(request):
    bridge = philip.HueBridge("192.168.115.110")
    lights = request.POST.getlist('lamp')

    if request.POST.get('main') == "toggle":
        bridge.on_off(lights)

    if request.POST.get('main') == "apply":
        hue = int(request.POST.get('hue')) # translation not complete
        bri = int(request.POST.get('bri'))
        sat = int(request.POST.get('sat'))
        bridge.change_hue(lights, hue)
        bridge.change_bri(lights, bri)
        bridge.change_sat(lights, sat)

    context = {
        'lights': bridge.get_lights(),
        'light_state': bridge.get_light_state()
    }

    return render(request, 'index.html', context=context)
