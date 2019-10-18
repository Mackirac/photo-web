from math import log
from PIL import Image

def ilog (image):
    return image.point(lambda p: int(255 * log(1 + p / 255, 2)))

def ipow (image, exp):
    return image.point(lambda p: int(255 * pow(p / 255, exp)))

def modify_interval (image, i1, i2):
    def set_interval(p):
        if i1[0] <= p and p <= i1[1]:
            return int(i2[0] + (p - i1[0]) * (i2[1] - i2[0]) / (i1[1] - i1[0]))
        return p
    return image.point(set_interval)

def negative (image):
    return image.point(lambda p: abs(p - 255))
