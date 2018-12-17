from random import randint
import os
"""
Sfunctions.py:
    Auxiliary functions for main program. To get correct format data.
"""
__author__ = "Maria Fernanda Gonzalez Chavez"
__maintainer__ = "Maria Ximena Lezama Hernandez"
__email__ = "fernandagch@ciencias.unam.mx lezama@ciencias.unam.mx"
__copyright__ = "Copyright 2018"
__version__ = "0.1"

class Pokemon:
    """
        POKEMON CLASS
        :param id: pokemon's id.
        :param name: pokemon's name.
        :param capture: ratio of capture in percent.
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

    pokemon = DB.readlines()[:line][    :param ]
    pokemon = pokemon.strip().split(",")

    return Pokemon(*pokemon)

def check_user(usr, pwd):
    """
        Check that a user already exists and that the password is correct.
        :param usr: user name.
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
        :param pokemon: obtained string from a Pokemon object.
        :param user: user name
    """
    users = open("DB/POKEDEX/"+user+".txt", "a")
    users.write(str(pokemon))
    users.write("_______________________________________")

def pokedex(user):
    """
        Return all the pokemons catched by the user.
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