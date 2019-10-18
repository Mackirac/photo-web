from django.views.decorators.csrf import csrf_exempt
from matplotlib import pyplot as plt
from django.http import HttpResponse
from io import BytesIO
from PIL import Image
import base64
import json

from .transformations.filters import Filter, MEAN, GAUSSIAN, LAPLACIAN1, LAPLACIAN2
from .transformations import\
    intensity,\
    steganography,\
    histogram,\
    convolution,\
    color,\
    non_linear

def decode_image (image):
    image = BytesIO(base64.b64decode(image))
    return Image.open(image)

def encode_image (image):
    b = BytesIO()
    image.save(b, 'PNG')
    return base64.b64encode(b.getvalue())

def build_response (body):
    res = HttpResponse(body)
    res['Content-Type'] = 'image/png'
    res['Access-Control-Allow-Origin'] = '*'
    return res

@csrf_exempt
def log (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(intensity.ilog(b)))
    return res

@csrf_exempt
def negative (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(intensity.negative(b)))
    return res

@csrf_exempt
def pow (request, factor):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(intensity.ipow(b, float(factor))))
    return res

@csrf_exempt
def parts (request, Ii, If, Fi, Ff):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(intensity.modify_interval(b, (Ii, If), (Fi, Ff))))
    return res

@csrf_exempt
def hide (request, text):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(steganography.hide_message(b, text)))
    return res

@csrf_exempt
def seek (request):
    b = decode_image(request.POST['image'])
    res = build_response(steganography.seek_message(b))
    res['Content-Type'] = 'text/plain'
    return res

@csrf_exempt
def get_hist (request):
    b = decode_image(request.POST['image'])
    hist = histogram.get_histogram(b)
    if len(hist) < 3:
        plt.bar(range(256), hist[0])
    else:
        plt.subplot(131)
        plt.bar(range(256), hist[0])
        plt.subplot(132)
        plt.bar(range(256), hist[1])
        plt.subplot(133)
        plt.bar(range(256), hist[2])

    b = BytesIO()
    fig = plt.gcf()
    fig.set_size_inches(18, 8)
    plt.savefig(b, dpi=100)
    plt.clf()
    plt.cla()
    h = base64.b64encode(b.getvalue())
    res = build_response(h)
    return res

@csrf_exempt
def equalize (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(histogram.equalize(b)))
    return res

@csrf_exempt
def conv (request, filter):
    b = decode_image(request.POST['image'])
    filter = json.loads(filter)
    filter = Filter(filter['dx'], filter['dy'], filter['values'], filter['divisor'])
    return build_response(encode_image(convolution.conv(b, filter, True)))

@csrf_exempt
def mean (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(convolution.conv(b, MEAN, True)))
    return res

@csrf_exempt
def gaussian (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(convolution.conv(b, GAUSSIAN, True)))
    return res

@csrf_exempt
def median (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(non_linear.nmedian(b, 1, 1)))
    return res

@csrf_exempt
def laplace1 (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(convolution.conv(b, LAPLACIAN1, True)))
    return res

@csrf_exempt
def laplace2 (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(convolution.conv(b, LAPLACIAN2, True)))
    return res

@csrf_exempt
def high_boost (request, k):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(non_linear.high_boost(b, k)))
    return res

@csrf_exempt
def grayscale (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(color.grayscale(b)))
    return res

@csrf_exempt
def weighted_grayscale (request, p1, p2, p3):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(color.weighted_grayscale(b, (
        float(p1), float(p2), float(p3)
    ))))
    return res

@csrf_exempt
def sepia (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(color.sepia(b)))
    return res

@csrf_exempt
def sobel (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(non_linear.sobel(b)))
    return res

@csrf_exempt
def binarize (request, threshold):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(non_linear.binarize(b, threshold)))
    return res

@csrf_exempt
def harm_mean (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(non_linear.harm_mean(b)))
    return res
