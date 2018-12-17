from random import randint
import os

"""
    POKEMON CLASS
    - id : pokemon's id.
    - name : pokemon's name.
    - capture : ratio of capture in percent. 
    - scurry : pokemon's capacity to go away.
"""
class Pokemon:
    def __init__(self, id, name, capture, scurry):
        self.id = id
        self.name = name
        self.capture = int(capture)
        self.scurry = int(scurry)

    """
        Return a string with the pokemon information.
    """
    def __str__(self):
        s  = "idPokemon: "+self.id+"\n"
        s += "Name: "+self.name+"\n"
        s += "Capture: "+str(self.capture)+"\n"
        s += "Scurry: "+str(self.scurry)+"\n"

        return s

    """
        Returns the corresponding image to the pokemon in byte format.
    """
    def get_image(self):
        src = "POKEMONS/"+self.id+".png"
        print(src)
        with open(src, "rb") as imageFile:
            f = imageFile.read()
            b = bytearray(f)
        return b

"""
    Return an aleatory Pokemon object.
"""
def get_pokemon():
    DB = open("DB/POKEMON.txt","r")
    line = randint(1,50)

    pokemon = DB.readlines()[:line][-1]
    pokemon = pokemon.strip().split(",")

    return Pokemon(*pokemon)

"""
    Check that a user already exists and that the password is correct.
    - usr : user name.
    - pwd : password user.
    if the is no user corresponding to the data returns False.
"""
def check_user(usr, pwd):
    users = open("DB/USERS.txt","r")
    user_data = users.readline()
    while user_data:
        user, password = user_data.strip().split(",")
        if user == usr and password == pwd:
            return user
        user_data = users.readline()
    return False

"""
    Save the catched pokemon in the register of the actual user.
    - pokemon : obtained string from a Pokemon object.
    - user : user name 
"""
def add_pokemon_to_pokedex(pokemon, user):
    users = open("DB/POKEDEX/"+user+".txt", "a")
    users.write(str(pokemon))
    users.write("_______________________________________")

"""
    Return all the pokemons catched by the user.
    - user : user name
"""
def pokedex(user):
    path = "DB/POKEDEX/"+user+".txt"

    if not os.path.isfile(path):
        print("AAA")
        result = "Seems you have not captured any pokemon ):\n"
        result += "_______________________________________"
    else:
        with open(path, "r") as POKEDEX:
            result = POKEDEX.read()

    return result