from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from io import BytesIO
from PIL import Image
import base64

@csrf_exempt
def index (request):
    b = request.POST['image']
    b = base64.b64decode(b)
    b = BytesIO(b)
    b = Image.open(b)
    b.show()
    res = HttpResponse('WH')
    res['Access-Control-Allow-Origin'] = '*'
    return res
