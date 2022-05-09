import atexit
import os
from datetime import datetime

import bcrypt

from Database import Database

from User import User
from src.Protocols import UserManagment
from src.Protocols.UserManageProtocol import UserManageProtocol


def create_bitmask():
    f = open("bitmask", "x")
    f = open("bitmask", "w")
    f.write(bcrypt.hashpw(str(admin.bitmask).encode("utf-8"), bcrypt.gensalt()).hex())
    f.close()


atexit.register(create_bitmask)


def client_select():
    global user_ptr
    t = 0
    while True:
        print("[1] Login\n[2] Logout\n[3] Register\n[4] Delete")
        a = input("? ")
        print(a)
        if a == "1":
            if user_ptr is None:
                print("logging in")
                user_ptr = UserManageProtocol(t, datetime.now(), db, UserManagment.UserManagment.LOGIN,
                                       user_ptr).run_protocol()
                if user_ptr:
                    print("Logging successful")
                    user_ptr.cmd_input()
                else:
                    print("Logging in unsuccessful. Please try again")
                    t += 1
            else:
                user_ptr.cmd_input()
        elif a == "2":
            c = UserManageProtocol(t, datetime.now(), db, UserManagment.UserManagment.LOGOUT, user_ptr).run_protocol()
            if c:
                print("successfully logged out")
            else:
                t += 1
        elif a == "3":
            print("registering")
        elif a == "4":
            print("deleting")


db = Database()
admin = User(True, db.wallets[0], "admin", db)
os.environ["_BITMASK"] = bcrypt.hashpw(str(admin.bitmask).encode("utf-8"),
                                       bcrypt.gensalt()).hex()

user1 = User(False, db.wallets[1], "user1", db)
user_ptr = None
print("UniPy Client v0.0.1 Please select operation:")
client_select()
