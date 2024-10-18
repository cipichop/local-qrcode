# local-qrcode
Locally generate or read a qr code for any text or link or anything...

## CREATE
`python createqr.py url output`

    url         URL to generate QR code
    output      Output file name
usage example:
`python createqr.py https://github.com out.png`

## READ
`python readqr.py qr`

    qr          QR code image to be read
usage example:
`python readqr.py out.png`