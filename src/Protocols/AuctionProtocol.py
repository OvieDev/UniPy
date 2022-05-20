import asyncio
import string
from datetime import datetime
import random

from src.Database import Database
from src.Item import Item
from src.Protocol import Protocol
from src.ProtocolException import ProtocolException
from src.User import User

import bcrypt


class AuctionProtocol(Protocol):
    def __init__(self, signer: User, identify: int, time: datetime, db: Database, initial_bid: float, until: datetime,
                 item_sold: Item):
        super().__init__(signer, identify, time, db)
        self.__initial = initial_bid
        self.bid = initial_bid
        self.auction_until = until
        self.auctionid = bcrypt.kdf(str(random.choices(string.ascii_letters, k=32)).encode(), bcrypt.gensalt(), 22, 32)
        self.holder = None
        self.item = item_sold

    def run_protocol(self):
        try:
            print(
                f"Creating an auction requires you to pay: {self.bid * 0.1 + self.signer.wallet.currency.dollar_to_coin(1 * (self.auction_until.hour - self.time.hour))} {self.signer.wallet.currency.name}")
            a = input("Do you really want to create an auction? [y/n] ")
            if a.lower() == "y":
                if self.signer.wallet.pay_and_return_value(self.bid * 0.1 + self.signer.wallet.currency.dollar_to_coin(
                        1 * (self.auction_until.hour - self.time.hour))) == 0:
                    raise ProtocolException(self, "Cannot proceed the payment")
                else:
                    asyncio.run(self.bid_loop())
        except ProtocolException as e:
            print(e)

    # TODO: Do something with bid loop cuz i don't know how async works lol :)
    async def bid_loop(self):
        while True:
            await asyncio.sleep(1)
            # if datetime.now() >= self.auction_until:
            #     if self.holder is not None:
            #         self.holder.items.append(self.item)
            #         self.signer.items.remove(self.item)
            #         del self
            #     else:
            #         self.signer.wallet.accept_income(self.signer.wallet.hash, self.__initial)
