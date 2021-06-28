from Packets.Messages.Server.TeamMessage import TeamMessage

from Utils.Reader import BSMessageReader
from database.DataBase import DataBase


class TeamSetLocationMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.player.mapID = self.read_Vint()

    def process(self):
        DataBase.replaceValue(self, 'mapID', self.player.mapID)
        TeamMessage(self.client, self.player).send()