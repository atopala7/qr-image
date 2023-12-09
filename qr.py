#!/usr/bin/env python

"""
QR Code Generator Script

This script generates a QR code for a given URL and optionally pastes an image in the center.
 
Usage: python qr.py <url> [<image>]

Parameters:
  - <url>: The URL for which the QR code will be generated.
  - [<image>]: Optional parameter. If provided, the image will be pasted in the center of the QR code.
"""

import sys
import qrcode
from PIL import Image, ImageDraw

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Usage: python qr.py <url> [<image>]")
    sys.exit(1)

url = sys.argv[1]

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
)

QRcode.add_data(url)

QRcode.make()

img = QRcode.make_image().convert('RGB')

if len(sys.argv) == 3:
    try:
        logo = Image.open(sys.argv[2])
    except:
        print("Error: Invalid image")
        sys.exit(1)

    logo = logo.resize((80, 90), resample=Image.Resampling.NEAREST, reducing_gap=3.0)

    position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

    draw = ImageDraw.Draw(img)
    # draw.ellipse((position[0] - 1, position[1] + 2, position[0] + logo.size[0] + 1, position[1] + logo.size[1] - 3), fill=(255, 255, 255))
    draw.rectangle((position[0] - 5, position[1], position[0] + logo.size[0] + 4, position[1] + logo.size[1]), fill=(255, 255, 255))

    img.paste(logo, position, mask=logo)

img.save('qr.png')

print("QR code generated successfully!")
sys.exit(0)