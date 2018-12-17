from PIL import Image
import io
import os

"""
    Saves the image of the catched pokemon in a directory named as the user.
    - id : pokemon's id
    - user : user name
    - image_data : pokemon's image in byte array
"""
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