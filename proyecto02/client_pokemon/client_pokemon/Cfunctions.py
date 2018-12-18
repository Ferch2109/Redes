#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import io
import os

"""
    package.module
    ==============
    Cfunctions.py:
        Auxiliary functions for main program. To get correct format data.

    Autors:     Maria Fernanda Gonzalez Chavez y Maria Ximena Lezama Hernandez
    Email:      fernandagch@ciencias.unam.mx lezama@ciencias.unam.mx"
    Version     "0.1"
    :copyright:   2018
"""

def save_and_show_image(id,user,image_data):
    """
        Saves the image of the catched pokemon in a directory named as the user.
       :type id: string
       :param id: pokemon's id
       :type user: string
       :param user: user name
       :type image_data: bytearray
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