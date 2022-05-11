import datetime
import os
import bcrypt

from src.Currency import Currency
from src.Database import Database
from src.Protocol import Protocol
from src.ProtocolException import ProtocolException
from src.Protocols.UserManagment import UserManagment
from src.User import User
from src.Wallet import Wallet


class UserManageProtocol(Protocol):
    def __init__(self, identify: int, time: datetime.datetime, db: Database, inout: UserManagment, ptr, signer=None):
        super().__init__(signer, identify, time, db, name="UserManager")
        self.direction = inout
        self.client_pointer = ptr
        print(self.direction)

    def run_protocol(self):
        try:
            if self.direction == UserManagment.LOGIN and self.client_pointer is None:
                login = input("Enter your public key: ")
                for i in self.database.connected_users:
                    if i.public_key.hex() == login:
                        login = input("Enter wallet hash: ")
                        if login == i.wallet.hash:
                            if os.getenv("_BITMASK"):
                                if bcrypt.checkpw(str(i.bitmask).encode("utf-8"),
                                                  bytes.fromhex(os.environ["_BITMASK"])):
                                    self.signer = i
                                    return i
                                else:
                                    raise ProtocolException(self, "Invalid Bitmask")
                            else:
                                raise ProtocolException(self, "Invalid bitmask")
                        else:
                            raise ProtocolException(self, "Cannot find user")
                else:
                    raise ProtocolException(self, "Cannot find user")

            elif self.direction == UserManagment.LOGOUT and self.client_pointer is not None:
                r = input("Are you sure you want to logout? [y/n] ")
                if r.lower() == "y":
                    self.client_pointer = None
                    return True
                else:
                    print("Cancelled!")
                    return False
            elif self.direction == UserManagment.REGISTER:
                username = input("Please choose your username: ")

                if 5 > len(username) > 25:
                    raise ProtocolException(self, "Username too small or too large")

                w_hash = input("Please select your wallet hash: ")

                if not len(w_hash) > 8 and not len(w_hash) < 22:
                    raise ProtocolException(self, "Wallet hash to small or too large")

                currency = input("Please choose your currency: ")

                if len(currency) != 3:
                    raise ProtocolException(self, "Invalid currency")
                c = Currency.get_currency_from_str(self.database, currency)
                wallet = Wallet(c, w_hash, 0, "Wallet")
                u = User(False, wallet, username, self.database)
                self.database.connected_users.append(u)
                print("User created!")
                return u

            elif self.direction == UserManagment.DELETE and self.client_pointer is not None:
                a = input("Are you sure you want to delete your account? [y/n] ")
                if a.lower() == "y":
                    print("Attempting deletion!")
                    money = self.client_pointer.wallet.amount
                    self.client_pointer.wallet.currency.add_to_stash(money)
                    self.client_pointer.wallet.amount = 0
                    self.database.connected_users.remove(self.client_pointer)
                    print("Successfully deleted account")
                    return None
            else:
                raise ProtocolException(self, "Unknown User Managment Action")
        except ProtocolException as e:
            print(e)
            return False
