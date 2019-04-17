#! /usr/bin/python
# 8.2 Basics of Using PIL/PILLOW

# Some basic usage of PIL/PILLOW

from PIL import Image


# Resizing image
def resize_images(image_names, new_size=(200, 200)):
    # This will go through the images and resize them
    for image_name in image_names:
        img = Image.open(image_name)
        img = img.resize(new_size)
        img.save("resized_" + image_name)


images = ["butterfly.jpg", "python.jpg", "red_sky.jpg"]
resize_images(images)

# Cropping image
# The crop function takes 4 arguments the first one is width and second is height
python_img = Image.open("python.jpg")
python_img.show()
python_img = python_img.crop((100, 100, 300, 300))
python_img.show()

# Rotation
# Using the rotate() function and giving how much and it rotates
butterfly = Image.open("butterfly.jpg")
butterfly = butterfly.rotate(90)
butterfly.show()