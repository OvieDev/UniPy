import asyncio
import string
from datetime import datetime
import random

from src import User
from src.Database import Database
from src.Events.Event import subscribe_to_event
from src.Item import Item
from src.Protocol import Protocol
from src.ProtocolException import ProtocolException

import bcrypt


class AuctionProtocol(Protocol):
    def __init__(self, signer: User, identify: int, time: datetime, db: Database, initial_bid: float, until: datetime,
                 item_sold: Item):
        super().__init__(signer, identify, time, db)
        self.__initial = initial_bid
        self.bid = initial_bid
        self.auction_until = until
        self.auctionid = bcrypt.kdf(str(random.choices(string.ascii_letters, k=32)).encode(), bcrypt.gensalt(), 22,
                                    32).hex()
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
                    print(self.auctionid)
                    self.database.auctions.append(self)
            else:
                del self
        except ProtocolException as e:
            print(e)

    @staticmethod
    @subscribe_to_event("on_auction_bid")
    def on_bid(kwargs, opt_args, *args):
        for i in opt_args["db"].auctions:
            if i.auctionid == opt_args["auction"] and opt_args["money"] > i.bid:
                if opt_args["bidder"].wallet.pay_and_return_value(
                        opt_args["bidder"].wallet.currency.dollar_to_coin(opt_args["money"])) is True:
                    i.bid = opt_args["money"]
                    i.holder = opt_args["bidder"]
                    print(f"Success! {i.auctionid} {i.bid}")
                    break
                else:
                    print("Cannot bid!")
        else:
            print("Cannot find auction")
