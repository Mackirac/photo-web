from PIL import Image
import numpy as np

class Filter:
    def __init__ (self, dx, dy, data, divisor):
        if len(data) != (1 + 2*dx) * (1 + 2*dy):
            raise Exception("Invalid data length")
        if divisor == 0: raise Exception("0 divisor error")
        self.dx, self.dy, self.data, self.divisor =\
            dx, dy, tuple(data), divisor
    
    def print (self):
        print(self.dx)
        print(self.dy)
        print(self.data)
        print(self.divisor)

def get_neighborhood(image, x, y, dx, dy):
    neighborhood = []
    for y in range(y - dy, y + dy + 1):
        for x in range(x - dx, x + dx + 1):
            try:
                neighborhood.append(np.array(image.getpixel((x, y))))
            except IndexError:
                neighborhood.append(np.array([0] * len(image.getbands())))
    return list(reversed(neighborhood))

def apply_filter (image, x, y, filter):
    neighborhood = get_neighborhood(image, x, y, filter.dx, filter.dy)
    pixel = np.array([0] * len(image.getbands()))
    for i in range(len(neighborhood)):
        pixel += neighborhood[i] * filter.data[i]
    return tuple(map(lambda p: int(p / filter.divisor), pixel))

def conv (image, filter):
    black = tuple([0] * len(image.getbands()))
    output = Image.new(image.mode, image.size, black)
    for x in range(image.width):
        for y in range(image.height):
            output.putpixel((x, y), apply_filter(image, x, y, filter))
    return output

im = Image.open('images/image.bmp')
im.show()
conv(im, Filter(1, 1, np.array([
    0, -1, 0,
    -1, 0, 1,
    0, 1, 0
]), 1)).show()
