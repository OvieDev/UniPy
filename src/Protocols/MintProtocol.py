from datetime import datetime
from typing import Union

from src import User
from src.Currency import Currency
from src.Database import Database
from src.Item import Item
from src.Protocol import Protocol
from src.ProtocolException import ProtocolException


# Item Types:
# True: Item
# False: Currency
class MintProtocol(Protocol):
    def __init__(self, signer: User, identify: int, time: datetime, db: Database, amount: Union[int, float],
                 it_type: bool, it_name: str):
        super().__init__(signer, identify, time, db, name="Minting Protocol")
        self.item_type = it_type
        self.amount = amount
        self.itemname = it_name

    def run_protocol(self):
        try:
            if self.item_type is True and self.amount is float or self.amount < 1:
                raise ProtocolException(self, "Invalid token amount")

            if self.item_type is False and self.amount <= 0.5:
                raise ProtocolException(self, "Invalid currency amount")

            if self.item_type is False:
                short = input("Give a shortcut for a currency (3 letters): ")
                if len(short) > 3:
                    raise ProtocolException(self, "Shortcut too long")

                m = input("How much the currency is worth: ")
                desc = input("Give description for your currency")
                if self.signer.wallet.pay_with_dollars(float(m) * self.amount) == 0:
                    raise ProtocolException(self, "Cannot proceed payment. Amount too high")
                curr = Currency(self.itemname, self.signer, desc, self.amount, float(m))
                self.database.currencies[short] = curr
            else:
                m = input("How much item is worth [in dollars]: ")
                d = {}
                a = ""
                while True:
                    try:
                        a = input("Tag name (-e or empty string if you want to quit): ")
                        if a == "-e" or len(a) == 0:
                            raise AttributeError
                        v = input("Enter tag value: ")
                        d[a] = v
                    except AttributeError:
                        break
                if self.signer.wallet.pay_with_dollars(float(m) * self.amount + len(d)) == 0:
                    raise ProtocolException(self, "Cannot proceed payment. Amount too high")
                self.signer.items.append(Item(self.itemname, self.signer, int(self.amount), d, float(m)))
        except ProtocolException as e:
            print(e)
