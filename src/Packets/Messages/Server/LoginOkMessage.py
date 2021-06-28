import time

from Utils.Writer import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104

    def encode(self):
        self.writeInt(0)  # High ID
        self.writeInt(self.player.LowID)  # Low ID
        
        self.writeInt(0)  # High ID
        self.writeInt(self.player.LowID)  # Low ID
        
        self.writeString(self.player.Token)  # Token
        self.writeString()
        self.writeString()
        
        self.writeInt(13)
        self.writeInt(283)
        self.writeInt(0)
        
        self.writeString("dev")
        
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeString()
        
        print("[*] Message LoginOk has been sent.")