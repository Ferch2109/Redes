#cliente
from multiprocessing.connection import Client
from pickle import dumps
from states import Automata
from CODES import START, CATCH, MSG
from functions import save_and_show_image

host = "localhost"
port = 9999

#print("Write IP Dir:")
#host = input()

while host != "localhost":
  print("Error: Wrong IP - Try again...\n")
  print("Write IP Dir:")
  host = input()


sock = Client((host, port))

automata = Automata(sock)

# Success conexion.
automata.recive()

CODE = 0
"""     START OF GAME     """

#State: S0
while True:
  if CODE == 0:
    # Goto(S0, 10) -> S1
    automata.gotoS(dumps([10,START]),[10])

    # S2
    automata.recive()

    # Goto(S2, 20) -> S3
    automata.gotoS(dumps([20,CATCH]),[30,31,32])

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
  # SH
  elif CODE == 24:
    """   Goto: S3 | S4   """
    # Goto(SH, 31) -> S4
    # Goto(SH, 32) -> S3
    automata.gotoS(dumps([0, MSG]), [31, 32])
  # S6
  elif CODE == 23:
    """   Goto: S3 | S4   """
    # Goto(S6, 31) -> S4
    # Goto(S6, 32) -> S3
    automata.gotoS(dumps([0,MSG]), [31, 32])
  # S7
  elif CODE == 22:
    save_and_show_image(automata.name,automata.image)
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

