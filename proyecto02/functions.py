from random import randint
from PIL import Image
import io

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
        src = "pokemons/"+self.id+".png"
        print(src)
        with open(src, "rb") as imageFile:
            f = imageFile.read()
            print("AM")
            b = bytearray(f)
            print("BM")
        return b


def get_pokemon():
    DB = open("DB/POKEMON.txt","r")
    line = randint(1,50)

    pokemon = DB.readlines()[:line][-1]
    pokemon = pokemon.strip().split(",")

    return Pokemon(*pokemon)

def save_and_show_image(name,image_data):
    image = Image.open(io.BytesIO(image_data))
    #path = "pokedex/"+id_usr+"/"+name+".png"
    path = "pokedex/"+name+".png"
    image.save(path)
    image.show()