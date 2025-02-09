from phue import Bridge


b = Bridge('192.168.178.35')
b.connect()
b.get_api()

def on_off():
    print(b.get_light(1, 'on'))
    if not b.get_light(1, 'on'):
        b.set_light([1,4], 'on', True)
    else:
        b.set_light([1,4], 'on', False)