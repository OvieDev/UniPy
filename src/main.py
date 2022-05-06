from datetime import datetime

from Database import Database

from User import User
from src.Protocols import UserManagment
from src.Protocols.UserManageProtocol import UserManageProtocol


def client_select():
    print("[1] Login\n[2] Logout\n[3] Register\n[4] Delete")
    a = input("? ")
    if a=="1":
        print("logging in")
        c = UserManageProtocol(0, datetime.now(), db, UserManagment.UserManagment.LOGIN, user_ptr).run_protocol()
        if c:
            print("Logging successful")
    elif a=="2":
        print("logging out")
    elif a=="3":
        print("registering")
    elif a=="4":
        print("deleting")
    else:
        client_select()


db = Database()
admin = User(True, db.wallets[0], "admin", db)
user1 = User(False, db.wallets[1], "user1", db)
user_ptr = None
print("UniPy Client v0.0.1 Please select operation:")
client_select()
