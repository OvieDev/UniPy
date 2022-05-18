import atexit
import os
from datetime import datetime

import bcrypt

from src.User import User, Database
from src.Protocols import UserManagment
from src.Protocols.UserManageProtocol import UserManageProtocol


@atexit.register
def create_bitmask():
    try:
        f = open("bitmask", "x")
        f = open("bitmask", "w")
        f.write(bcrypt.hashpw(str(admin.bitmask).encode("utf-8"), bcrypt.gensalt()).hex())
        f.close()
    except Exception as e:
        print("Error when tried to create bitmask backup!")
        print(e)
        a = input("Would you like to try again? (Having a backup bitmask is a good idea) [y/n] ")
        if a.lower() == "y":
            create_bitmask()


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
                user_ptr = None
                print("successfully logged out")
                create_bitmask()
            else:
                t += 1
        elif a == "3":
            print("registering")
            user_ptr = UserManageProtocol(t, datetime.now(), db, UserManagment.UserManagment.REGISTER,
                                          user_ptr).run_protocol()
        elif a == "4":
            print("deleting")
            user_ptr = UserManageProtocol(t, datetime.now(), db, UserManagment.UserManagment.DELETE,
                                          user_ptr).run_protocol()
            print(user_ptr)


db = Database.Database()
admin = User(True, db.wallets[0], "admin", db)
os.environ["_BITMASK"] = bcrypt.hashpw(str(admin.bitmask).encode("utf-8"),
                                       bcrypt.gensalt()).hex()

user1 = User(False, db.wallets[1], "user1", db)
user_ptr = None
print("UniPy Client v0.0.1 Please select operation:")
client_select()
