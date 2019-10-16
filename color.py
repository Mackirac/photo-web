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

def sepia (image):
    bands, mode, size, data =\
        len(image.getbands()), image.mode, image.size, list(image.tobytes())
    if bands < 3: raise TypeError("Image with less than 3 channels")

    for i in range(0, len(data), bands):
        pixel = (data[i], data[i+1], data[i+2])
        data[i] = int(0.393*pixel[0] + 0.769*pixel[1] + 0.189*pixel[2])
        if data[i] < 0: data[i] = 0
        if data[i] > 255: data[i] = 255

        data[i+1] = int(0.349*pixel[0] + 0.686*pixel[1] + 0.168*pixel[2])
        if data[i+1] < 0: data[i+1] = 0
        if data[i+1] > 255: data[i+1] = 255

        data[i+2] = int(0.272*pixel[0] + 0.534*pixel[1] + 0.131*pixel[2])
        if data[i+2] < 0: data[i+2] = 0
        if data[i+2] > 255: data[i+2] = 255
    return Image.frombytes(mode, size, bytes(data))
