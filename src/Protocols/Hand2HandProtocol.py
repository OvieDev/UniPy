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
            if i.public_key.hex() == reciever:
                self.reciever = i
                break
        else:
            for y in self.signer.shortcuts:
                if y.username == self.reciever:
                    self.reciever = y
                    break
            else:
                self.reciever = None
        self.items = items[0]

    def run_protocol(self):
        try:
            if self.reciever is None:
                raise ProtocolException(self, "Cannot fetch wallet")
            if self.reciever == self.signer:
                raise ProtocolException(self, "You cannot send money to yourself")
            if len(self.items) == 0:
                raise ProtocolException(self, "Invalid credentials")

            total_curr = 0.0
            it = []
            for i in self.items:
                if i[:2] == "T_":
                    for z in self.signer.items:
                        if z.token == i:
                            it.append(z)
                    else:
                        raise ProtocolException(self, "You don't own item, with this token: " + i)
                elif i[len(i) - 1] == "$" and float(i[:-1]):
                    total_curr += float(i[:-1]) / float(self.signer.wallet.currency.dollar_price)
                elif float(i):
                    total_curr = float(i)
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
            self.reciever.items.extend(it)
            for i in it:
                self.signer.items.remove(i)
            # register to transactions
            self.database.proto_archive.append({
                "protocol_id": self.id,
                "protocol_name": self.name,
                "protocol_signtime": self.time,
                "protocol_signer": self.signer.public_key,
                "success": self.valid,
                "details": [
                    "Hand2Hand Protocol HEADER",
                    f"Reciever: {self.reciever}",
                    f"sent_items: {it}"
                ]
            })
            self.database.emit_server_message(
                f"{self.signer.public_key.hex()} sent {self.reciever.public_key.hex()} {total_curr} {self.reciever.wallet.currency.name}")

        except ProtocolException as e:
            self.valid = False
            print(e)
            self.database.proto_archive.append({
                "protocol_id": self.id,
                "protocol_name": self.name,
                "protocol_signtime": self.time,
                "protocol_signer": self.signer.public_key.hex(),
                "success": self.valid,
                "details": [
                    "Hand2Hand Protocol HEADER",
                    f"Reciever: {self.reciever}"
                ]
            })

    def dollar_str_to_float(self, string):
        if string[len(str) - 1] == "$":
            return string[:-1]
