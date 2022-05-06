import datetime

from src.Database import Database
from src.Protocol import Protocol
from src.ProtocolException import ProtocolException
from src.Protocols.UserManagment import UserManagment
from src.User import User


class UserManageProtocol(Protocol):
    def __init__(self, identify: int, time: datetime.datetime, db: Database, inout: UserManagment, ptr, signer=None):
        super().__init__(signer, identify, time, db)
        self.direction = inout
        self.client_pointer = ptr

    def run_protocol(self):
        try:
            if self.direction == UserManagment.LOGIN and self.client_pointer is None:
                login = input("Enter your public key: ")
                for i in self.database.connected_users:
                    if i.public_key.hex() == login:
                        login = input("Enter wallet hash: ")
                        if login == i.wallet.hash:
                            self.signer = i
                            return i
                        else:
                            raise ProtocolException(self, "Cannot find user")
                else:
                    raise ProtocolException(self, "Cannot find user")
            elif self.direction == UserManagment.LOGOUT:
                pass
            elif self.direction == UserManagment.REGISTER:
                pass
            elif self.direction == UserManagment.DELETE:
                pass
            else:
                raise ProtocolException(self, "Unknown User Managment Action")
        except ProtocolException as e:
            print(e)
            return False
