import string
import random

import bcrypt

from src.Currency import Currency
from src.Protocol import Protocol, User, datetime, Database, ProtocolException

SALES = ()


class SalesProtocol(Protocol):
    def __init__(self, signer: User, identify: int, time: datetime.datetime, db: Database, money: float,
                 currency: Currency, callback):
        super().__init__(signer, identify, time, db)
        self.saleid = f"SALE{bcrypt.kdf(str(random.choices(string.ascii_letters, k=25)).encode(), bcrypt.gensalt(), 25, 40).hex()}"
        self.callback = callback
        self.money = money
        self.currency = currency
        self.earned_money = 0.0
        global SALES
        l = list(SALES).append(self)
        SALES = tuple(l)

    def run_protocol(self, payer: User):
        try:
            if payer.wallet.currency == self.signer.wallet.currency:
                val = payer.wallet.pay_and_return_value(self.money)
            else:
                val = payer.wallet.pay_and_return_value(self.signer.wallet.convert_from_currency(payer.wallet.currency,
                                                                                                 self.money) + payer.wallet.currency.dollar_to_coin(
                    15))
            if val is not False:
                self.earned_money += val
                self.callback()
            else:
                raise ProtocolException(self, "Cannot proceed payment")
        except ProtocolException as e:
            print(e)

    @staticmethod
    def pay_for_saleID(saleid: str, payer: User):
        global SALES
        for i in SALES:
            if saleid == i.saleid:
                i.run_protocol(payer)
                break
        else:
            print("Couldn't find the right sale")
