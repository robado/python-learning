#! /usr/bin/python
# 8.4 Custom Picture Manipulation

# Negating image
# Each pixel has red, green and blue color component.
from PIL import Image

butterfly_img = Image.open("butterfly.jpg")
butterfly_img.show()

# So in this function we have to get every pixel from an image and minus 255 from red, green and blue pixels. 255 is
# because every pixel has value of 0 to 255. To negate an image we have to minus 255 from every pixel
width, height = butterfly_img.size  # (w, h)
for x in range(width):
    for y in range(height):
        pixel_coordinate = (x, y)
        # if png then you have to add alpha
        r, g, b = butterfly_img.getpixel(pixel_coordinate)

        negative_color = (255 - r, 255 - g, 255 - b)
        butterfly_img.putpixel(pixel_coordinate, negative_color)

butterfly_img.show()
