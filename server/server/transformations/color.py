from PIL import Image

def grayscale (image):
    output, data, bands = [], image.tobytes(), len(image.getbands())
    if bands < 3: return image

    for idx in range(0, len(data), bands):
        pixel = data[idx]
        pixel += data[idx+1]
        pixel += data[idx+2]
        output.append(int(pixel / 3))
        for a in range(3, bands): output.append(data[idx+a])

    return Image.frombytes('L', image.size, bytes(output))

def weighted_grayscale (image, weights):
    output, data, bands = [], image.tobytes(), len(image.getbands())
    if bands < 3: return image
    if len(weights) != 3: raise ArithmeticError("Invalid number of weights")
    if round(abs(sum(weights) - 0.00001)) != 1: raise ArithmeticError("Non-normal weights")

    for idx in range(0, len(data), bands):
        pixel = data[idx] * weights[0]
        pixel += data[idx+1] * weights[1]
        pixel += data[idx+2] * weights[2]
        output.append(int(pixel))
        for a in range(3, bands): output.append(data[idx+a])

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
