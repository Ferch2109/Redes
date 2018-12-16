from pickle import dumps, loads

from CODES import ERROR

class Automata:
    def __init__(self, socket, server=False):
        self.socket = socket
        self.server = server
        self.code = 0
        self.name = ""
        self.image = None
    """
        Goto(S_{act},code) -> S_{next} or Goto(S0,*/{10}) -> S60
    """
    def gotoS(self, data, codes=[]):
        if self.server:
            self.socket.send(data)
            return

        data = loads(data)
        msg = data[1]

        code = input(msg)

        """There can't be this error from server"""
        # Goto(S0, * / {10}) -> S60
        while int(code) not in codes:
            print(ERROR(60), "\n")
            print(msg)
            code = input()

        self.socket.send(dumps([int(code), "-"]))

    def recive(self):
        data = self.socket.recv()
        data = loads(data)
        print("LEN",len(data))

        if data[0] != 0:
            print("\nCode_recived:", data[0])
            self.code = int(data[0])

        print(data[1])

        if len(data) > 2:
            self.name = data[2]
            self.image = data[3]

    def end(self):
        print("Good Bye!!")
        self.socket.close()