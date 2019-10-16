from PIL import Image

def grayscale (image):
    output, bands = [], len(image.getbands())
    if bands == 1: return image

    for y in range(image.height):
        for x in range(image.width):
            ipixel = image.getpixel((x, y))
            opixel = 0
            for c in range(bands):
                opixel += ipixel[c]
            output.append(int(opixel / bands))
    return Image.frombytes('L', image.size, bytes(output))

def weighted_grayscale (image, weights):
    output, bands = [], len(image.getbands())
    if bands == 1: return image
    if len(weights) != bands: raise IndexError("Unmathing weights and bands length")
    if sum(weights) != 1: raise ArithmeticError("Non-normal weights")

    for y in range(image.height):
        for x in range(image.width):
            ipixel = image.getpixel((x, y))
            opixel = 0
            for c in range(bands):
                opixel += ipixel[c] * weights[c]
            output.append(int(opixel))
    return Image.frombytes('L', image.size, bytes(output))
