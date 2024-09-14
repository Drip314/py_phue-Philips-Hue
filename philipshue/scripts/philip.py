from phue import Bridge


b = Bridge('192.168.115.110')
b.connect()
b.get_api()


def on_off():
    b.set_light([1, 2], 'on', not b.get_light(1, 'on'))
