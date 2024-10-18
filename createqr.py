#!/usr/bin/python3
import qrcode
import argparse

parser = argparse.ArgumentParser(description='Locally generate QR code for a given URL')
parser.add_argument('url', type=str, help='URL to generate QR code')
parser.add_argument('output', type=str, help='Output file name')

args = parser.parse_args()

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, border=3)

url = args.url
qr.add_data(url)
qr.make()

QRimg = qr.make_image(
	fill_color="black", back_color="white").convert('RGB')

QRimg.save(args.output)

print('QR code generated!')
