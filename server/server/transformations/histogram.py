from PIL import Image
import matplotlib.pyplot as plt

def get_histogram (image):
    hists, channels = [], image.getbands()
    for c in range(len(channels)):
        hist = [0] * 256
        for p in image.getdata(c): hist[p] += 1
        hists.append(hist)
    return hists

def acumulate (hists):
    for i in range(1, 256):
        for hist in hists: hist[i] += hist[i-1]
    return hists

def equalize (image):
    hists = acumulate(get_histogram(image))
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            if isinstance(pixel, tuple):
                pixel = list(pixel)
                for c in range(len(hists)):
                    pixel[c] = int(hists[c][pixel[c]] * 255 / hists[c][len(hists[c]) - 1])
                pixel = tuple(pixel)
            else:
                pixel = int(hists[0][pixel] * 255 / hists[0][len(hists[0]) - 1])
            image.putpixel((x, y), pixel)
    return image
