from scripts import philip, HexToHue
from django.shortcuts import render


def myview(request):
    bridge = philip.HueBridge("192.168.115.110")
    lights = request.POST.getlist('lamp')
    light_ids = []
    for light in lights:
        light_ids.append(int(bridge.get_id_by_name(light)))

    if request.POST.get('main') == "toggle":
        bridge.on_off(lights)

    if request.POST.get('main') == "apply":
        hue = round((int(request.POST.get('hue')) / 360) * 65535)
        bri = round((int(request.POST.get('bri')) / 100) * 254)
        sat = round((int(request.POST.get('sat')) / 100) * 254)

        print(hue)
        print(bri)
        print(sat)

        bridge.change_hue(light_ids, hue)
        bridge.change_bri(light_ids, bri)
        bridge.change_sat(light_ids, sat)

    context = {
        'lights': bridge.get_lights(),
        'light_state': bridge.get_light_state()
    }

    return render(request, 'index.html', context=context)
