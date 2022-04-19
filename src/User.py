import os
import datetime

from Database import Database
from Wallet import Wallet
import Protocols.CommandSendProtocol

class User:
    def __init__(self, admin:bool, wallet:Wallet, name:str, db: Database):
        self.is_admin = admin
        self.miner = None
        self.wallet = wallet
        self.username = name
        self.db = db
        self.view = 0
        self.cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
        #self.public_key_name = f"{bcrypt.hashpw('adminpasswordlol'.encode('utf-8'), salt=bcrypt.gensalt(128))}".encode("utf-8").hex()
        #self.public_key_amount = 0
        #self.private_key_name = f"{bcrypt.hashpw('password'.encode('utf-8'), salt=bcrypt.gensalt(128))}".encode("utf-8").hex()
        #self.private_key_amount = 0

        print("Initializing new user: " + name)

#    def cmd_input(self):
#       anws = input(self.username + "/? ")
#        if anws == "help":
#            print("""
#             USER COMMANNDS:
#              - ses_create: Creates session for default wallet currency for 30$
#              - transactions: Preview all your transactions
#              - server_console (ADMIN-ONLY): Goes to the server
#              - cls (SERVER AND USER): Clears console
#
#             SERVER COMMANDS (ADMIN-ONLY):
#              - user_mode: Goes back to user view
#             """)
#         elif anws == "license":
#             print("""MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
# MMMMMMMMMWWMMMMMMMMMWNMMWX0NMMMMMMMMMMNKNMMMWNNNNNWWMMMMMMMN
# MMMMMMMM0:lXMMMMMMMXl;OM0;.;0WMMMMMMMMx.;KWk,'''''',;lKMMMMN
# MMMMMMMMx.'0MMMMMMM0'.xM0'  .xKNMMMMMMO. oWKkxd' ,oooxXMMMMN
# MMMMMMMMx.'0MMMMMMM0'.xMK; ,;..:KWMMMMX; cWMMMX; oWMMMMMMMMN
# MMMMMMMMx.'0MMMMMMMO..kMX; oNd;..dNMMMN: cNMMMK, dMMMMMMMMMN
# MMMMMMMMx.'0MMMMMMMx.'0MX; oMWW0:.;OWMNc cNMMMK, dMMMMMMMMMN
# MMMMMMMMO'.xMMMMMMX: cNMX; oMMMMNk'.:0Nc cWMMMK, dMMMMMMMMMN
# MMMMMMMMNl 'OWMMMNl.'0MMX; oWMMMMMXd..:' cWMMMK; oNNNWMMMMMN
# MMMMMMMMMXo'.;llc'.:0MMMK, oMMMMMMMWKl.  lW0l:,  .'''oNMMMMN
# MMMMWKkkOXWXOdolox0NMMMMXdl0MMMMMMMMMWKxdKMKdoodxxxkkKWMMMMN
# MMNx;.   .oXMMMMMMMN0kdolllodxkO0KXNNNWMMMMMMMMMMMMMMMMMMMMN
# MWo        :XMMMMWx,.            ...'',;lxKWWWWMMMMMMMMMMMMN
# MO.   ..   .dMMMMO.  .;:;'.               .cc,,dXMMMMMMMWXWN
# Wl    ,:    oWMMWl 'xXWMMWKd'             ..    oWMMMNOl,.;d
# X;     .   .xMMWx. :NMMNWMMMXo,.     ..   ,d'   .OMNx,     :
# k.        .dNMM0'   ,cc,;kWMMWNKxoox0K0c  cNd.   ,o,    .;xK
# o     ':cdKWMMWo         .c0WMMMMMMMMMNd. dMNl        .c0WMN
# l    .OMMMMMMMNc           .,lodxkOkdl,  .kMMNl     .c0WMMMN
# d    ,KMMMMMMMK,  ':lol;.      ...       :XMMWd.   ;KWMMMMMN
# O.   cNMMMMMWXo. :XWMMMW0c. .:xOXKc     .xMMMK,   .kMMMMMMMN
# WOllxXMMMMMWx'   'x00KWMMWXO0NMMMMk.    :XMMWo    cNMMMMMMMN
# MMMMMMMMMMMX;      ...:ONMMMMMMWXx'    '0MMM0'   .OMMMMMMMMN
# MMMMMMMMMMMWk.          ':loolc;.     .kMMMMK:  .oNMMMMMMMMN
# MMMMMMMMMMMMMKo,......               .xWMMMMMNOkKWMMMMMMMMMN
# MMMMMMMMMMMMMMMWXK0KK0kxdolllooolcccd0WMMMMMMMMMMMMMMMMMMMMN
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
# MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
#
#
# By Ovie
# """)
#         elif anws=="cls":
#             print("Clearing!")
#             time.sleep(0.5)
#             self.cls()
#         elif self.view == 0:
#             if anws == "ses_create":
#                 print("Creating session for default wallet currency...")
#                 if self.wallet.pay_with_dollars(30) > 0:
#                     self.db.add_session(self.wallet.currency)
#                 else:
#                     print("Can't create session. Required amount of currency must be worth at least 30$")
#
#             elif anws == "transactions":
#                 self.wallet.transactions()
#
#             elif anws == "server_console":
#                 if self.view == 0 and self.is_admin is True:
#                     print("Going to server console")
#                     time.sleep(0.5)
#                     print(self.view)
#                     self.view=1
#                     self.cls()
#                     self.show_previous_log()
#                 else:
#                     print("You do not have such permissions")
#
#         elif anws == "user_mode" and self.view == 1:
#             print("Going to user mode")
#             time.sleep(0.5)
#             self.cls()
#             self.view=0
#
#         else:
#             print("You're currently in server mode")
#
#         self.cmd_input()

    def cmd_input(self):
        while True:
            cmd = input("?/ ")
            cmd_list = cmd.split(" ")
            arg_list = cmd_list.copy()
            arg_list.pop(0)
            if len(arg_list)==0:
                proto = Protocols.CommandSendProtocol.CommandSendProtocol(self, 0, datetime.datetime.now(), self.db, cmd_list[0])
            else:
                proto = Protocols.CommandSendProtocol.CommandSendProtocol(self, 0, datetime.datetime.now(), self.db, cmd_list[0], arg_list)
            proto.run_protocol()

    def server_log(self, dbmes):
        if self.view == 1:
            print(dbmes)

    def show_previous_log(self):
        for i in self.db.log:
            print(i)
