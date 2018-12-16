from PIL import Image
import io
import os

def save_and_show_image(id,user,image_data):
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