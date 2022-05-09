import os
import random
from datetime import datetime


def help_command(arg, proto):
    print("""
                 USER COMMANNDS:
                  - ses_create: Creates session for default wallet currency for 30$
                  - transactions: Preview all your transactions
                  - server_console (ADMIN-ONLY): Goes to the server
                  - cls (SERVER AND USER): Clears console
    
                 SERVER COMMANDS (ADMIN-ONLY):
                  - user_mode: Goes back to user view
                 """)


def clear_command(arg, proto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Cleared!")


def ses_create_command(arg, proto):
    if len(arg[0]) != 3:
        raise IndexError("Currency name too short or too long (must be 3 characters long)")
    print("Session created")


def server_mode_move_command(arg, proto):
    if proto.signer.view == 0:
        print("Going to server view!")
        proto.signer.view = 1
    else:
        print("Going to user view!")
        proto.signer.view = 0


def pay_command(arg, proto):
    from src.Protocols.Hand2HandProtocol import Hand2HandProtocol
    h2h = Hand2HandProtocol(proto.signer, random.randint(0, 99999999), datetime.now(), proto.database, arg[0], [arg[1]])
    h2h.run_protocol()


def client_command(arg, proto):
    return True
