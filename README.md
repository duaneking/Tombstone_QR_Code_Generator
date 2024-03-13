# Tombstone_QR_Code_Generator
Open Source Tombstone QR Code Generator

# Why This exists

Through some very sad circumstances I had the need to create code that could be used to generate an image of a QR Code that an engraver could then engrave on a tombstone.

This will fully replace what I would personally consider to be a predatory device sold by what I would personally consider to be a predatory company for the same purpose, and allow the grieving to have the lowest cost possible by being in full control of all hosting of any files that they may choose to direct people to.

This also has the added benefit of allowing them to use a qrcode to engrave a quote or memory directly into the stone without requiring a 3rd party hosting solution that can then be decoded with the proper tools if the QR code is made big enough.

# Warning
Explore the available settings and fully understand them `before` you engrave anything into stone.

# This project is DUAL Open source licensed and both must be respected.

This also means that if a private company uses this source code as part of a larger project, they must make that larger project source code public under the AGPL and follow all open source requirements.

The output PNG is not under AGPL or the AI restrictions. Only the project is.

# Environment Setup

Clone this code in git after installing a modern python development system.

Validate that you have python 3+ installed:

```
python3 --version
```

Create a clean virtual development environment named '.venv':

```
python3 -m venv .venv
```

Activate your virtual development environment on windows;

```
.venv\Scripts\activate
```

Activate your virtual development environment on linux or mac;

```
source .venv/bin/activate
```

Once you have a virtual environment set up install all the dependencies and validate they are installed:

```
pip install -r requirements.txt
pip freeze
```

# Generating a QR Code

Now you can create QR Codes.

To see options:
```
python qrcode_generate.py --help
```

To generate a QR Code with "https://github.com/duaneking/Tombstone_QR_Code_Generator" as its data with the highest amount of error checking in the smallest version that will hold it:

```
python qrcode_generate.py "https://github.com/duaneking/Tombstone_QR_Code_Generator" --output example_github_qr_code_dont_use_this_on_stone.png --code-version=6 --error-correction=H
```

# QR Code Versions and why they matter

QR code versions are supported from version 1 to version 40.

The version of a QR code denotes its size.
- Version 1 is the smallest at 21x21 modules (dots).  This is the default.
- Version 40 is the largest at 177x177 modules (dots).

Each higher version increases the size by 4 modules per side. 

Capacity: The data capacity of a QR code increases with its version number; capacity also varies based on the type of data encoded (numeric, alphanumeric, binary, or Kanji) and the error correction level used (see below).

# Error Correction Levels and why they really do matter
- L (Low): Recovers 7% of data.
- M (Medium): Recovers 15% of data.
- Q (Quartile): Recovers 25% of data.
- H (High): Recovers 30% of data. This is the default.

The higher error correction level you use, the longer this data will be available as the stone wears down over time from erosion (rain) and general weathering. At the same time this will also decreases the amount of data that you can save on the stone. This is because more space in the QR code is used for error correction. The good news is archeologists have found stone tablets from thousands of years ago that didn't have this technology, and they could still read them.

We can't fight time but we can put the engineering effort in to make sure that our loved ones are remembered for as long as possible.

# Data Capacity and Limitations
- Numeric Only: Up to 7,089 characters in Version 40 with L level.
- Alphanumeric: Up to 4,296 characters in Version 40 with L level.
- Binary/Byte: Up to 2,953 bytes (characters) in Version 40 with L level.
- Kanji/Kana: Up to 1,817 characters in Version 40 with L level.

These are hard limits.

Lower versions have significantly less capacity. For example, Version 1 can hold:

41 numeric, 25 alphanumeric, 17 binary, or 10 Kanji characters with L error correction.

# Making the qr code last.
Work with your `Stonesmith` and `Engraver` to get the correct dimensions and settings that you will need to create the image that they require.

Use the error correction value that fits what you want to happen.  By default, it's set to the highest possible error correction value and the smallest size; that may be too much for you. Lower it if you want a smaller QR code. This is intentionally done so that you can do the work needed to make sure the QR code is as small as possible for your use case as there is no one size fits all solution for this.

If this is done well you will not need to buy a 3rd party device that is little more than a plaque with a printed QR code designed to trap you. The stone itself can be the plaque.

If a company doesn't make the terms of the hosting agreement for any kind of content clear up front or pretends like a third party is handling that, always be suspicious.

When you are done and need to use the terminal for other things type `deactivate` to deactivate the virtual development environment, or just close the command window.
