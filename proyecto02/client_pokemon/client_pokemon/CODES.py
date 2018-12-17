def ERROR(code):
    switcher = {
        60: "ERROR: Wrong code. Select one code from the options...",
        61: "ERROR: Start of session failed. Incorrect info.\nTry again...\n",
        62: "ERROR: Conecting to database.\n"
    }

    return switcher.get(code)

def SESSION(code):
    switcher = {
        70: "Asking for start session...\n",
        71: "SESSION STARTED!\n",
        72: "SEE POKEMONS in POKEDEX...\n",
        73: "Showing POKEDEX:\n"
    }

    return switcher.get(code)

START = "Ask for a Pokemon to catch it!\n"

def SERVER(code=0,k = 0, id_pok = "",name = ""):
    switcher = {
        20: "A WILD "+name.upper()+" HAS APPERED!!\nidPokemon: "+id_pok+"\n",
        21: "WANT TO TRY AGAIN?\nidPokemon:"+id_pok+"\n"+str(k)+" remaining attemps..\n",
        22: "YOU DID IT!\nYOUR POKEMON WAS SAVED\n",
        23: "SORRY, YOU DON'T HAVE MORE ATTEMPS! :(",
        24: "OMG! "+name.upper()+" GO AWAY! :(",
    }

    return switcher.get(code)

def CLIENT(code):
    switcher = {
        30: "YES!\n",
        31: "NO.\n",
        32: "FINISH CONECTION.\n"
    }

    return switcher.get(code)

PRINCIPAL = "WHAT DO YOU WANT TO DO?\n\t[10] "+START+"\t[72] "+SESSION(72)

CATCH = "DO YOU WANT TO CATCH THE POKEMON?\n"
CATCH += "\t[30] "+CLIENT(30)+"\t[31] "+CLIENT(31)+"\t[32] "+CLIENT(32)

MSG = "DO YOU STILL WANT TO PLAY?\n"
MSG += "\t[31] "+CLIENT(30)+"\t[32] "+CLIENT(31)