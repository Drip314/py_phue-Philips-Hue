import colorsys


class Color:
    def __init__(self, hex_value):
        self.hex_value = str(hex_value)
        if not self.hex_value.startswith('#') or len(self.hex_value) > 7:
            print("[ERROR] invalid HEX-value received.")
            raise ValueError(f"Invalid HEX value. {self.hex_value} is not a valid HEX-value.")

    def to_rgb(self):
        return int(self.hex_value[1] + self.hex_value[2], 16), int(self.hex_value[3] + self.hex_value[4], 16), int(
            self.hex_value[5] + self.hex_value[6], 16)

    def to_hue(self):
        r, g, b = self.to_rgb()
        return int(colorsys.rgb_to_hls(r, g, b)[0] * 65535)


if __name__ == "__main__":
    x = Color('#60ab3e')
    print(x.to_hue())
