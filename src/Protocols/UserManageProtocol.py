import datetime
import os
import bcrypt

from src.Database import Database
from src.Protocol import Protocol
from src.ProtocolException import ProtocolException
from src.Protocols.UserManagment import UserManagment


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
                r = input("Are you sure you want to logout? [y/n]")
                if r.lower() == "y":
                    self.client_pointer = None
                    return True
                else:
                    print("Cancelled!")
                    return False
            elif self.direction == UserManagment.REGISTER:
                # TODO register
                pass
            elif self.direction == UserManagment.DELETE:
                # TODO delete
                pass
            else:
                raise ProtocolException(self, "Unknown User Managment Action")
        except ProtocolException as e:
            print(e)
            return False
