from random import randint


class Pokemon:
    def __init__(self, id, name, capture, scurry):
        self.id = id
        self.name = name
        self.capture = int(capture)
        self.scurry = int(scurry)

    def __str__(self):
        s  = "idPokemon: "+self.id+"\n"
        s += "Name: "+self.name+"\n"
        s += "Capture: "+str(self.capture)+"\n"
        s += "Scurry: "+str(self.scurry)+"\n"

        return s

    def get_image(self):
        src = "POKEMONS/"+self.id+".png"
        print(src)
        with open(src, "rb") as imageFile:
            f = imageFile.read()
            b = bytearray(f)
        return b


def get_pokemon():
    DB = open("DB/POKEMON.txt","r")
    line = randint(1,50)

    pokemon = DB.readlines()[:line][-1]
    pokemon = pokemon.strip().split(",")

    return Pokemon(*pokemon)

def check_user(usr, pwd):
    users = open("DB/USERS.txt","r")
    user_data = users.readline()
    while user_data:
        user, password = user_data.strip().split(",")
        if user == usr and password == pwd:
            return user
        user_data = users.readline()
    return False

def add_pokemon_to_pokedex(pokemon, user):
    users = open("DB/POKEDEX/"+user+".txt", "a")
    users.write(str(pokemon))
    users.write("_______________________________________")

def POKEDEX(user):
    path = "DB/POKEDEX/"+user+".txt"

    with open(path, "r") as POKEDEX:
        return POKEDEX.read()