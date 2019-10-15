from PIL import Image
import numpy as np

class Filter:
    def __init__ (self, dx, dy, data, divisor):
        if len(data) != (1 + 2*dx) * (1 + 2*dy):
            raise Exception("Invalid data length")
        if divisor == 0: raise ZeroDivisionError()
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
    return pixel / filter.divisor

def conv (image, filter):
    bands = len(image.getbands())
    output = []
    minp, maxp = [0] * bands, [0] * bands
    for y in range(image.height):
        for x in range(image.width):
            pixel = apply_filter(image, x, y, filter)
            for c in range(bands):
                if pixel[c] < minp[c]: minp[c] = pixel[c]
                if pixel[c] > maxp[c]: maxp[c] = pixel[c]
                output.append(pixel[c])
    for idx in range(0, len(output), bands):
        for c in range(bands):
            output[idx + c] -= minp[c]
            output[idx + c] *= 255 / (maxp[c] - minp[c])
            output[idx + c] = int(output[idx + c])
    return Image.frombytes(image.mode, image.size, bytes(output))
