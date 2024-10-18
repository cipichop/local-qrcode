#!/usr/bin/python3
from PIL import Image
from pyzbar.pyzbar import decode
import argparse

parser = argparse.ArgumentParser(description='Locally read QR code from an image')
parser.add_argument('qr', type=str, help='QR code image to be read')

args = parser.parse_args()

img = Image.open(args.qr)
data = img.load()

decoded = decode(img)
if decoded:
    print(decoded[0].data.decode('latin-1'))