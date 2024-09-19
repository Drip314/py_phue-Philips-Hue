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

    def get_id_by_name(self, light):
        return self.bridge.get_light_id_by_name(light)

    def get_parameter_state(self, param):
        lights = self.get_lights()
        light_states = []
        for i in range(0, len(lights)):
            light_states.append(self.bridge.get_light(lights[i].name, parameter=param))
        return light_states

    def change_state(self, lights, param, value):
        if len(lights) == 0:
            return
        self.bridge.set_light(lights, param, value)

    def get_light_state(self):
        return self.get_parameter_state('on')

    def get_hue(self):
        return self.get_parameter_state('hue')

    def get_bri(self):
        return self.get_parameter_state('bri')

    def on_off(self, lights):
        self.change_state(lights, 'on', not self.bridge.get_light(lights[random.randint(0, len(lights) - 1)], 'on'))

    def change_hue(self, lights, hue):
        print(lights)
        self.change_state(lights, 'hue', hue)

    def change_bri(self, lights, bri):
        self.change_state(lights, 'bri', bri)

    def change_sat(self, lights, lig):
        self.change_state(lights, 'sat', lig)


if __name__ == '__main__':
    b = HueBridge("192.168.115.110")
    b.get_light_state()
    b.on_off([1])
