from phue import Bridge
import random


class HueBridge:
    def __init__(self, ip):
        self.ip = str(ip)
        if not len(self.ip.split('.')) == 4:
            print("[ERROR] invalid IP.")
            raise ValueError(f"Invalid IP received.\n-> {self.ip} is not a valid IP!")
        self.bridge = Bridge(self.ip)
        self.bridge.connect()
        self.bridge.get_api()

    def get_lights(self):
        return self.bridge.lights

    def get_light_state(self):
        lights = self.get_lights()
        light_states = []
        for i in range(0, len(lights)):
            light_states.append(self.bridge.get_light(lights[i].name, 'on'))
        print(light_states)

    def on_off(self, lights):
        if len(lights) == 0:
            return
        self.bridge.set_light(lights, 'on', not self.bridge.get_light(lights[random.randint(0, len(lights) - 1)], 'on'))

    def change_brightness(self, lights, bri):
        if len(lights) == 0:
            return
        self.bridge.set_light(lights, 'bri', bri)

    def change_color(self, lights, hue):
        if len(lights) == 0:
            return
        self.bridge.set_light(lights, 'hue', hue)


if __name__ == '__main__':
    b = HueBridge("192.168.115.110")
    b.get_light_state()
