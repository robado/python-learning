#! /usr/bin/python
# 8.3 Picture Manipulation

from PIL import Image, ImageFilter, ImageEnhance

# All the interesting stuff about PIL/Pillow can be found at this site -> https://pillow.readthedocs.io/en/stable/index.html
butterfly = Image.open("butterfly.jpg")
# Grayscale. This simple makes image grayscale
grayscale = butterfly.convert('L')
grayscale.show()
# This shows edges
edge_detect = butterfly.filter(ImageFilter.FIND_EDGES)
edge_detect.show()
contrast = ImageEnhance.Contrast(butterfly).enhance(5.0)
bright = ImageEnhance.Brightness(contrast).enhance(100)
contrast.show()
bright.show()