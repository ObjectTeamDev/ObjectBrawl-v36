from Utils.Writer import Writer
from database.DataBase import DataBase
import random


class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        pass
        print("[*] Message TeamMessage has been sent.")
