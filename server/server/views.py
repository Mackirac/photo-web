from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from io import BytesIO
from PIL import Image
import base64

from .transformations.filters import MEAN, GAUSSIAN, LAPLACIAN1, LAPLACIAN2
from .transformations import\
    intensity,\
    histogram,\
    convolution,\
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
    res = build_response(encode_image(intensity.ipow(b, factor)))
    return res

@csrf_exempt
def parts (request, Ii, If, Fi, Ff):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(intensity.modify_interval(b, (Ii, If), (Fi, Ff))))
    return res

@csrf_exempt
def equalize (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(histogram.equalize(b)))
    return res

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
def sobel (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(non_linear.sobel(b)))
    return res

@csrf_exempt
def binarize (request, threshold):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(non_linear.binarize(b, threshold)))
    return res
