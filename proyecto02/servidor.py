#servidor
from multiprocessing.connection import Listener
import threading
from pickle import dumps
from states import Automata
from CODES import SERVER
from random import randint
from functions import get_pokemon, Pokemon

host = "localhost"
port = 9999

sock = Listener((host, port))
print ("Socket Created...")
print ("Socket now listening!\n")

def worker(*args):
    conn = args[0]
    addr = args[1]
    K = 7
    id_pokemon = ""
    name = ""
    try:
        print('Conexion with {}.'.format(addr))
        automata = Automata(conn, server=True)
        data = dumps([0,"Conexion success!\n"])
        automata.gotoS(data)

        CODE = 0
        while True:
            if CODE == 0:
                # Attemps
                K = 7
                # S1
                automata.recive()

                p = get_pokemon()
                data = [20, SERVER(code=20, id_pok=p.id, name=p.name)]
                # Goto(S1, 20) -> S2
                automata.gotoS(dumps(data))

            """     State: S3 | S4 | S5      """
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
                if randint(0,100) <= p.scurry:
                    print("SCURRY!")
                    # Goto(S5, 24) -> SH
                    data = dumps([24, SERVER(24,p.name)])
                    automata.gotoS(data)
                if K == 0:
                    print("NOATT!")
                    # Goto(S5, 23) -> S6
                    data = dumps([23, SERVER(23)])
                    automata.gotoS(data)
                elif randint(0,100) <= p.capture:
                    print("CAPTUREE!")
                    # Goto(S5, 22) -> S7
                    image_byte = p.get_image()
                    print(image_byte)
                    data = dumps([22,SERVER(22),p.name,image_byte])
                    automata.gotoS(data)
                    #automata.gotoS(22)
                else:
                    print("TRYAGAIN!")
                    # Goto(S5, 21) -> S8
                    data = dumps([21, SERVER(21,id_pok=p.id,k=K)])
                    automata.gotoS(data)
                    #automata.gotoS(21)

    except:
        conn.close()

while 1:
    conn = sock.accept()
    addr = sock.address
    threading.Thread(target=worker, args=(conn, addr)).start()

