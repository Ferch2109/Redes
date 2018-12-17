#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import io
import os
"""
Cfunctions.py:
    Auxiliary functions for main program. To get correct format data.
"""
__author__ = "Maria Fernanda Gonzalez Chavez"
__maintainer__ = "Maria Ximena Lezama Hernandez"
__email__ = "fernandagch@ciencias.unam.mx lezama@ciencias.unam.mx"
__copyright__ = "Copyright 2018"
__version__ = "0.1"

def save_and_show_image(id,user,image_data):
    """
        Saves the image of the catched pokemon in a directory named as the user.
       :param id: pokemon's id
       :param user: user name
       :param image_data: pokemon's image in byte array
    """
    if not os.path.exists("POKEDEX/"+user+"/"):
        os.mkdir("POKEDEX/"+user)

    path = "POKEDEX/" + user + "/" + id + ".png"

    if not os.path.exists(path):
        image = Image.open(io.BytesIO(image_data))
        #path = "POKEDEX/"+name+".png"
        image.save(path)
    else:
        image = Image.open(path)
    image.show()