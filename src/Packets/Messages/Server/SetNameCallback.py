from Utils.Writer import Writer
from database.DataBase import DataBase


class SetNameCallback(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVInt(201)
        self.writeString(self.player.name)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(-1)
        self.writeVInt(-1)
        self.writeVInt(0)
        self.writeVInt(0)
        DataBase.replaceValue(self, 'name', self.player.name)
        print("[*] Message SetNameCallback has been sent.")
