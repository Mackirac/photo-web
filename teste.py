from PIL import Image
from io import BytesIO
import base64

b = open('bytes')
b = base64.b64decode(b.read())
b = BytesIO(b)
b = Image.open(b)
b.show()
