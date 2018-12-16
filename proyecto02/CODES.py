def ERROR(code):
    switcher = {
        60: "ERROR: wrong code. Select one code from the options...",
        61: "ERROR: start of session failed...",
        62: "ERROR: conecting to database.\n"
    }

    return switcher.get(code)

def SESSION(code):
    switcher = {
        70: "Asking for start session...",
        71: "SESSION STARTED!\n",
        72: "Asking for pokemons in POKEDEX...",
        73: "Showing POKEDEX:\n"
    }

    return switcher.get(code)

START = "Ask for a Pokemon to catch it [10]:\n"

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

CATCH = "DO YOU WANT TO CATCH THE POKEMON?\n"
CATCH += "[30]"+CLIENT(30)+"[31]"+CLIENT(31)+"[32]"+CLIENT(32)

MSG = "DO YOU STILL WANT TO PLAY?\n"
MSG += "[31]"+CLIENT(30)+"[32]"+CLIENT(31)
