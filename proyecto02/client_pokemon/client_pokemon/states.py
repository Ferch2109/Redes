#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pickle import dumps, loads

from CODES import ERROR

class Automata:
    """
        AUTOMATON CLASS
        :param socket: socket through which the communication will be established.
        :param server: <boolean> indicates if the socket is a server socket.
    """
    def __init__(self, socket, server=False):
        self.socket = socket
        self.server = server
        self.code = 0
        # Name | User
        self.dat1 = ""
        # Image | Password
        self.dat2 = ""

    def gotoS(self, data, codes=[]):
        """
            Represent the function Goto in the automaton.
            Goto(S_{act},code) -> S_{next} or Goto(S0,*/{10}) -> S60
            :param data: data to send through the socket.
        """
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
        print(code)

        self.socket.send(dumps([int(code), "-"]))

    def recive(self):
        """
            Recive the data throught the socket.
        """
        data = self.socket.recv()
        data = loads(data)

        if data[0] != 0:
            print("\nCode_recived:", data[0])
            self.code = int(data[0])

        print(data[1])

        if len(data) > 2:
            self.dat1 = data[2]
            self.dat2 = data[3]

    def end(self):
        """
            End the conexión.
            FINAL STATE.
        """
        print("Good Bye!!")
        self.socket.close()