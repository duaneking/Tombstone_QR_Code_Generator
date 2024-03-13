"""
My honest opinion is that companies that claim that a qr code is hard to generate are acting in a predatory manner.

The following is as simple as I could get it to be.

- Duane of https://github.com/duaneking/Tombstone_QR_Code_Generator
"""

import argparse
import qrcode

# Setup command line argument parsing options
parser = argparse.ArgumentParser(description="Generate a QR code with custom options.")
parser.add_argument("data", type=str, help="The data to encode in the QR code.")
parser.add_argument("--fill-color", default="black", help="QR code fill color. Default is 'black'.")
parser.add_argument("--back-color", default="white", help="QR code background color. Default is 'white'.")
parser.add_argument("--box-size", type=int, default=10, help="The size of each box in the QR code in pixels. Default is 10.")
parser.add_argument("--border", type=int, default=4, help="The border size of the QR code in boxes. Default is 4.")
parser.add_argument("--fit", action='store_true', help="Fit the QR code to the data. Default is True.")
parser.add_argument("--code-version", default=1, help="The qr code version. larger numbers mean larger files. Default is 1. Max allowed is 40 and you probably don't need something that large.")
parser.add_argument('--error-correction', type=str, choices=['L', 'M', 'Q', 'H'], default='H', help='Error correction level: L (low), M (medium), Q (quartile), H (high). Default: H (high)')
parser.add_argument("--output", default="qr_code.png", help="Output file name. Default is 'qr_code.png'.")

# Parse input arguments
args = parser.parse_args()

# Map user input to qrcode.constants
error_correction_mapping = {
    'L': qrcode.constants.ERROR_CORRECT_L,
    'M': qrcode.constants.ERROR_CORRECT_M,
    'Q': qrcode.constants.ERROR_CORRECT_Q,
    'H': qrcode.constants.ERROR_CORRECT_H
}

# Get the correct library constant based on our user input.
error_correction_level = error_correction_mapping[args.error_correction]

# Create qr code instance using our custom options
qr = qrcode.QRCode(
    version=args.code_version,
    error_correction=error_correction_level,
    box_size=args.box_size,
    border=args.border,
)

# Add your QR Code data to the instance
qr.add_data(args.data)

try:
    qr.make(fit=args.fit)
except qrcode.exceptions.DataOverflowError as e:
    print(f"ERROR: QR Code generated was NOT big enough to save all the data. Try making the data smaller, using a lower error correction rate so you can fit more data into the qrcode, or use a higher qrcode version that supports holding more data. Check the readme if you want to know more about the settings available.")
    print(str(e))
    quit()

# Create an image from the QR Code instance using your custom colors
img = qr.make_image(fill_color=args.fill_color, back_color=args.back_color)

# Save the image to a file with the custom output filename
img.save(args.output)

print(f"QR Code generated and saved to {args.output}")
