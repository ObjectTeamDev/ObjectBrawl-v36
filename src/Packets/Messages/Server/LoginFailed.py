from Utils.Writer import Writer


class LoginFailed(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20103
        self.player = player
        self.reason = "бля"

    def encode(self):
        self.writeInt(0)  # error code 8 - update, 10 - maintenance
        self.writeString(self.reason)
        self.writeString(self.reason)
        self.writeString(self.reason)
        self.writeString(self.reason)  # update URL
        self.writeString(self.reason)
        self.writeHexa('''2E0000012C000000000000000000''')
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeVInt(0)
        print("[*] Message LoginFailed has been sent.")