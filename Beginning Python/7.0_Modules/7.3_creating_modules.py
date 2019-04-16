#! /usr/bin/python
# 7.3 Creating Modules

# Created the file volume.py

# import volumes
from volumes import *

# If I print the 'volumes' I can see what functions it has
# print(dir(volumes))

#print(volumes.cube_vol(2, 3, 4))

print(sphere_vol(4))

# So with this it is very good way to separate some functions if you don't want to include them in the main program.
# This way you can keep your main program clean!
