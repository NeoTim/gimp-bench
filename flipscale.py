#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re, glob
from gimpfu import *
from gimpenums import *

# our script
def my_script_function(image, drawable,  scale_w,  scale_h) :
    # print "."
    pdb.gimp_image_flip( image, ORIENTATION_HORIZONTAL )
    pdb.gimp_image_scale_full(image, scale_w, scale_h, INTERPOLATION_LANCZOS)
    drawable = pdb.gimp_image_flatten(image)
    pdb.plug_in_cartoon(image, drawable, 7, 0.2)
    pdb.plug_in_unsharp_mask(image, drawable, 1.0, 0.8, 0)
    pdb.plug_in_antialias(image, drawable)
    return

# This is the plugin registration function
register(
    "python_fu_flipscale",
    "Flip and scale image",
    "A simple Python Script that flips the image.",
    "Michel Ardan",
    "Michel Ardan Company",
    "May 2011",
    "<Image>/MyScripts/Flip And Scale Image",
    "*",
    [
         (PF_INT, 'scale_w', 'New width for the image', 100),
         (PF_INT, 'scale_h', 'New height for the image', 100)
    ],
    [],
    my_script_function,
)

main()
