import numpy as np
from math import sqrt
from PIL import Image
from convolution import Filter, conv, change_interval
from filters import GAUSSIAN as BLUR

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

def sobel (image):
    imh = list(conv(image, H, True).tobytes())
    imv = list(conv(image, V, True).tobytes())
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
