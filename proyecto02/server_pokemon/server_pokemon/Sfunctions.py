#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
import os
"""
    package.module
    ==============
    Sfunctions.py:
        Auxiliary functions for main program. To get correct format data.
        
    Autors:     Maria Fernanda Gonzalez Chavez y Maria Ximena Lezama Hernandez
    Email:      fernandagch@ciencias.unam.mx lezama@ciencias.unam.mx"
    Version     "0.1"
    :copyright:   2018
"""

class Pokemon:
    """
        POKEMON CLASS
        :type id: string
        :param id: pokemon's id.
        :type name: string
        :param name: pokemon's name.
        :type capture: int
        :param capture: ratio of capture in percent.
        :type scurry: int
        :param scurry: pokemon's capacity to go away.
        :returns: pokemon object.
    """
    def __init__(self, id, name, capture, scurry):
        self.id = id
        self.name = name
        self.capture = int(capture)
        self.scurry = int(scurry)

    def __str__(self):
        """
            :returns: String with the pokemon information.
        """
        s  = "idPokemon: "+self.id+"\n"
        s += "Name: "+self.name+"\n"
        s += "Capture: "+str(self.capture)+"\n"
        s += "Scurry: "+str(self.scurry)+"\n"

        return s

    def get_image(self):
        """
            :returns: corresponding image to the pokemon in byte format.
        """
        src = "POKEMONS/"+self.id+".png"
        print(src)
        with open(src, "rb") as imageFile:
            f = imageFile.read()
            b = bytearray(f)
        return b

def get_pokemon():
    """
        Get an aleatory pokemon from DB.
        :return: Pokemon object.
    """
    DB = open("DB/POKEMON.txt","r")
    line = randint(1,50)

    pokemon = DB.readlines()[:line][-1]
    pokemon = pokemon.strip().split(",")

    return Pokemon(*pokemon)

def check_user(usr, pwd):
    """
        Check that a user already exists and that the password is correct.
        :type usr: string
        :param usr: user name.
        :type pwd: string
        :param pwd: password user.
        :returns: False if the user is not in DB | wrong password.
    """
    users = open("DB/USERS.txt","r")
    user_data = users.readline()
    while user_data:
        user, password = user_data.strip().split(",")
        if user == usr and password == pwd:
            return user
        user_data = users.readline()
    return False

def add_pokemon_to_pokedex(pokemon, user):
    """
        Save the catched pokemon in the register of the actual user.
        :type pokemon: object Pokemon
        :param pokemon: obtained string from a Pokemon object.
        :type user: string
        :param user: user name
    """
    users = open("DB/POKEDEX/"+user+".txt", "a")
    users.write(str(pokemon))
    users.write("_______________________________________\n")

def pokedex(user):
    """
        Return all the pokemons catched by the user.
        :type user: string
        :param user: user name
        :returns: string of all the pokemons catched by the user.
    """
    path = "DB/POKEDEX/"+user+".txt"

    if not os.path.isfile(path):
        print("AAA")
        result = "Seems you have not captured any pokemon ):\n"
        result += "_______________________________________"
    else:
        with open(path, "r") as POKEDEX:
            result = POKEDEX.read()

    return result