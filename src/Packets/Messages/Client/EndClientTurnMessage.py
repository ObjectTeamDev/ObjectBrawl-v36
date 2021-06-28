from Utils.Reader import BSMessageReader
from Packets.Messages.Server.TeamMessage import TeamMessage
from database.DataBase import DataBase


class EndClientTurn(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player
        self.commandID = 0

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.commandID = self.read_Vint()

    def process(self):
        if self.commandID == 506:
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.player.brawlerID = self.read_Vint()
            DataBase.replaceValue(self, 'brawlerID', self.player.brawlerID)
