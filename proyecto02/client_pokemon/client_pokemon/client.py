#cliente
from multiprocessing.connection import Client
from pickle import dumps
from states import Automata
from CODES import START, CATCH, MSG, SESSION,PRINCIPAL
from Cfunctions import save_and_show_image

"""
client.py:
    MAIN PROGRAM
"""
__author__ = "Maria Fernanda Gonzalez Chavez"
__maintainer__ = "Maria Ximena Lezama Hernandez"
__email__ = "fernandagch@ciencias.unam.mx lezama@ciencias.unam.mx"
__copyright__ = "Copyright 2018"
__version__ = "0.1"
#host = "localhost"
#port = 9999

print("Write IP Dir:")
host = input()
print("Write PORT:")
port = input()

#while host != "localhost" or port != "9999":
while port != "9999":
  print("Error: Wrong PORT [should be 9999]...\n")
  print("Write IP Dir:")
  host = input()
  print("Write PORT:")
  port = input()

port = int(port)

try:
    sock = Client((host, port))
except:
    print("Can't connect to that dir IP.")
    exit(404)

automata = Automata(sock)

# Success conexion.
automata.recive()

SSESSION = False

print("USER:")
usr = input()
print("PASS:")
pwd = input()

"""   SESSION     """
#State: K1
print(SESSION(70))
# Goto(K1, 70) -> K2
sock.send(dumps([70, "-",  usr,pwd]))

# State: K3
while not SSESSION:
  automata.recive()

  #Goto S0
  if automata.code == 71:
    SSESSION = usr
  elif automata.code == 61:
    print("USER:")
    usr = input()
    print("PASS:")
    pwd = input()
    # Goto(K3, 70) -> K2
    sock.send(dumps([70, "-", usr, pwd]))

CODE = 0
PLAY = False
"""     START OF GAME     """
#State: S0
while SSESSION:
  if CODE == 0:
    """     Goto S1 | K4     """
    # Goto(S0, 10) -> S1
    # Goto(S0, 72) -> K4
    automata.gotoS(dumps([0, PRINCIPAL]), [10, 72])

    automata.recive()

    # Goto S0
    if automata.code == 73:
        PLAY = False
        print(automata.dat1)
        continue
    # S2
    elif automata.code == 20:
        PLAY = True
        """     Goto S3 | S4 | S5       """
        # Goto(S2, 32) -> S3
        # Goto(S2, 31) -> S4
        # Goto(S2, 30) -> S5
        automata.gotoS(dumps([0,CATCH]),[30,31,32])

  if PLAY:
    automata.recive()
    CODE = automata.code
    """     State: SF | S0 | S6 | S7 | S8     """

    # SF
    if CODE == 11:
        automata.end()
        break
    # S0
    elif CODE == 40:
        CODE = 0
        continue
    # S6
    elif CODE == 23 or CODE == 24:
        """   Goto: S3 | S4   """
        # Goto(S6, 31) -> S4
        # Goto(S6, 32) -> S3
        automata.gotoS(dumps([0,MSG]), [31, 32])
    # S7
    elif CODE == 22:
        save_and_show_image(automata.dat1,SSESSION,automata.dat2)
        """   Goto: S3 | S4   """
        # Goto(S6, 31) -> S4
        # Goto(S6, 32) -> S3
        automata.gotoS(dumps([0,MSG]), [31, 32])

    # S8
    elif CODE == 21:
        # Goto(S8, 30) -> S5
        # Goto(S8, 31) -> S4
        # Goto(S8, 32) -> S3
        automata.gotoS(dumps([0,CATCH]), [30, 31, 32])

