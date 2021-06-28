import time

from Utils.Writer import Writer


class ServerHello(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20100

    def encode(self):
        self.writeHexa('''00000018000000000000000000000000000000000000000000000000''')
        print("[*] Message ServerHello has been sent.")