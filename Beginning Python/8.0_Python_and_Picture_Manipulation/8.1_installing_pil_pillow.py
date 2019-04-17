#! /usr/bin/env python
# 8.1 Installing PIL/Pillow

# Site from where to intall https://pillow.readthedocs.io/en/stable/installation.html
# Site from to download 'PIP' https://pip.pypa.io/en/stable/

from PIL import Image
# Displaying image
red_sky = Image.open('red_sky.jpg')
# When this is ran it will show the image