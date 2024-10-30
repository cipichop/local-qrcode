# Create and Read QR Code in Python3
Locally generate or read a qr code for any text or link or anything...

## SET UP
Make sure you have python3 installed

Run: `pip install -r requirements.txt`

## CREATE QR

`python createqr.py url output`

    url         URL to generate QR code
    output      Output file name

usage sample:

`python createqr.py https://github.com out.png`

## READ QR

`python readqr.py qr`

    qr          QR code image to be read

usage sample:

`python readqr.py out.png`