from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from io import BytesIO
from PIL import Image
import base64

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
def index (request):
    b = decode_image(request.POST['image'])
    res = build_response(encode_image(b.point(lambda p: 0)))
    return res
