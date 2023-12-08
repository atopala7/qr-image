import sys
import qrcode
from PIL import Image, ImageDraw

if (len(sys.argv) != 3):
    print("Usage: python qr.py <image_path> <url>")
    sys.exit(1)

try:
    logo = Image.open(sys.argv[1])
except:
    print("Error: Invalid image")
    sys.exit(1)

logo = logo.resize((80, 90), resample=Image.Resampling.NEAREST, reducing_gap=3.0)
url = sys.argv[2]

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
)

QRcode.add_data(url)

QRcode.make()

img = QRcode.make_image().convert('RGB')

position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

draw = ImageDraw.Draw(img)
draw.ellipse((position[0] - 2, position[1] + 2, position[0] + logo.size[0] + 2, position[1] + logo.size[1] - 2), fill=(255, 255, 255))
img.paste(logo, position, mask=logo)
img.save('qr.png')

print("QR code generated successfully!")
sys.exit(0)