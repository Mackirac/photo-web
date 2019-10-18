import numpy as np
from math import sqrt
from PIL import Image
from statistics import median
from .filters import GAUSSIAN as BLUR
from .convolution import Filter, conv, change_interval, get_neighborhood

H = Filter(1, 1, [
    1, 0, -1,
    2, 0, -2,
    1, 0, -1
], 1)

V = Filter(1, 1, [
    -1, -2, -1,
     0,  0,  0,
     1,  2,  1
], 1)

def sobel (image, normalize=True):
    if normalize:
        imh = list(conv(image, H, True).tobytes())
        imv = list(conv(image, V, True).tobytes())
    else:
        imh = conv(image, H, False)
        imv = conv(image, V, False)

    output, bands = [], len(image.getbands())
    minp, maxp = [0] * bands, [0] * bands

    for idx in range(0, len(imh), bands):
        for c in range(bands):
            pixel = sqrt(pow(imh[idx + c], 2) + pow(imv[idx + c], 2))
            if pixel < minp[c]: minp[c] = pixel
            if pixel > maxp[c]: maxp[c] = pixel
            output.append(pixel)
    
    change_interval(output, bands, (minp, maxp))
    return Image.frombytes(image.mode, image.size, bytes(output))

def high_boost (image, k):
    blur = conv(image, BLUR, False)
    mask = np.array(list(image.tobytes())) - blur
    data, bands, output = image.tobytes(), len(image.getbands()), []

    for idx in range(0, len(data), bands):
        for c in range(bands):
            px = int(data[idx+c] + mask[idx+c] * k)
            if px < 0: px = 0
            if px > 255: px = 255
            output.append(px)

    return Image.frombytes(image.mode, image.size, bytes(output))

def nmedian (image, dx, dy):
    output = []
    for y in range(image.height):
        for x in range(image.width):
            neighborhood = get_neighborhood(image, x, y, dx, dy)
            try:
                neighborhood = zip(*neighborhood)
                for c in neighborhood:
                    output.append(int(median(c)))
            except TypeError:
                output.append(int(median(neighborhood)))
    return Image.frombytes(image.mode, image.size, bytes(output))

def binarize (image, threshold, gradient=False):
    def filter (p):
        if p >= threshold: return 255
        else: return 0
    if not gradient: image = sobel(image)
    return image.point(filter)
