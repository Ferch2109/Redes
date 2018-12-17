#servidor
from multiprocessing.connection import Listener
import threading
from pickle import dumps
from states import Automata
from CODES import SERVER, SESSION, ERROR
from random import randint
from Sfunctions import get_pokemon, check_user, pokedex
from Sfunctions import add_pokemon_to_pokedex

host = "localhost"
port = 9999

sock = Listener((host, port))
print("Socket Created...")
print("Socket now listening!\n")

def worker(*args):
    conn = args[0]
    addr = args[1]
    K = 7
    PLAY =  False
    SSESSION = False
    try:
        print('Conexion with {}.'.format(addr))
        automata = Automata(conn, server=True)
        data = dumps([0,"Conexion success!\n"])
        automata.gotoS(data)

        # K2
        while not SSESSION:
            automata.recive()

            if automata.code == 70:
                SSESSION = check_user(automata.dat1, automata.dat2)

            if SSESSION:
                # Goto(K2, 71) -> S0
                automata.gotoS(dumps([71,SESSION(71)]))
            else:
                # Goto(K2, 61) -> K3
                automata.gotoS(dumps([61, ERROR(61)]))

        CODE = 0
        POKEMON = None
        while SSESSION:
            if CODE == 0:
                # Attemps
                K = 7

                automata.recive()
                # S1
                if automata.code == 10:
                    PLAY = True
                    POKEMON = get_pokemon()
                    data = [20, SERVER(code=20, id_pok=POKEMON.id, name=POKEMON.name)]
                    # Goto(S1, 20) -> S2
                    automata.gotoS(dumps(data))
                #K4
                elif automata.code == 72:
                    PLAY = False
                    POKEDEX = pokedex(SSESSION)
                    data = [73, SESSION(73),POKEDEX,"\n"]
                    # Goto(K4, 73) -> S0
                    automata.gotoS(dumps(data))


            """     State: S3 | S4 | S5      """
            if PLAY:
                automata.recive()
                CODE = automata.code

                # S3
                if CODE == 32:
                    # Goto(S3, 11) -> SF
                    automata.gotoS(dumps([11,"-"]))
                # S4
                elif CODE == 31:
                    # Goto(S4, 40) -> S0
                    CODE = 0
                    automata.gotoS(dumps([40,"-"]))
                # S5
                elif CODE == 30:
                    K -= 1
                    """     Goto: S8 | S7 | S6      """
                    if randint(0,100) <= POKEMON.scurry:
                        #print("SCURRY!")
                        # Goto(S5, 24) -> S6
                        data = dumps([24, SERVER(24,name=POKEMON.name)])
                        automata.gotoS(data)
                    elif K == 0:
                        #print("NOATT!")
                        # Goto(S5, 23) -> S6
                        data = dumps([23, SERVER(23)])
                        automata.gotoS(data)
                    elif randint(0,100) <= POKEMON.capture:
                        #print("CAPTUREE!")
                        add_pokemon_to_pokedex(POKEMON, SSESSION)
                        # Goto(S5, 22) -> S7
                        image_byte = POKEMON.get_image()
                        #print(image_byte)
                        data = dumps([22,SERVER(22),POKEMON.id,image_byte])
                        automata.gotoS(data)
                        #automata.gotoS(22)
                    else:
                        #print("TRYAGAIN!")
                        # Goto(S5, 21) -> S8
                        data = dumps([21, SERVER(21,id_pok=POKEMON.id,k=K)])
                        automata.gotoS(data)
                        #automata.gotoS(21)

    except:
        conn.close()

while 1:
    conn = sock.accept()
    addr = sock.address
    threading.Thread(target=worker, args=(conn, addr)).start()

