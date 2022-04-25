import datetime

from src.Database import Database
from src.Protocol import Protocol
from src.ProtocolException import ProtocolException
from src.User import User


class Hand2HandProtocol(Protocol):
    def __init__(self, signer: User, identify: int, time: datetime.datetime, db: Database, reciever,
                 items: list, name="Hand2Hand"):
        super().__init__(signer, identify, time, db, name=name)
        for i in self.database.connected_users:
            if i.username == reciever:
                self.reciever = i
                break
        else:
            self.reciever = None
        self.items = items

    def run_protocol(self):
        try:
            print(self.items)
            if self.reciever is None:
                raise ProtocolException(self, "Cannot fetch wallet")
            if len(self.items) != 1:
                raise ProtocolException(self, "Invalid credentials")

            total_curr = 0.0
            for i in self.items:
                if float(i):
                    total_curr = float(i)
                if i[len(i) - 1] == "$" and float(i[:len(i) - 1]):
                    total_curr += float(i[:len(i) - 1])
                else:
                    pass

            if self.reciever.wallet.currency != self.signer.wallet.currency:
                ret = self.signer.wallet.pay_and_return_value(total_curr)
                if ret == 0:
                    raise ProtocolException(self, "H2H cannot proceed payment - too high amount")

                print(f"Transaction successful! Paid: {total_curr} of {self.signer.wallet.currency.name}")
                total_curr = self.reciever.wallet.convert_from_currency(self.signer.wallet.currency, total_curr)
                self.reciever.wallet.accept_income(self.reciever.wallet.hash, total_curr)
            else:
                ret = self.signer.wallet.pay_and_return_value(total_curr)
                if ret == 0:
                    raise ProtocolException(self, "H2H cannot proceed payment - too high amount")
                self.reciever.wallet.accept_income(self.reciever.wallet.hash, total_curr)
            # register to transactions
            self.database.proto_archive.append({
                "protocol_id": self.id,
                "protocol_name": self.name,
                "protocol_signtime": self.time,
                "protocol_signer": self.signer.public_key_name,
                "success": self.valid,
                "details": [
                    "Hand2Hand Protocol HEADER",
                    f"Reciever: {self.reciever}"
                ]
            })

        except ProtocolException as e:
            self.valid = False
            print(e)
            self.database.proto_archive.append({
                "protocol_id": self.id,
                "protocol_name": self.name,
                "protocol_signtime": self.time,
                "protocol_signer": self.signer.public_key_name,
                "success": self.valid,
                "details": [
                    "Hand2Hand Protocol HEADER",
                    f"Reciever: {self.reciever}"
                ]
            })
