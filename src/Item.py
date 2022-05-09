import base64

import bcrypt
import random

from src.User import User

chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"


class Item:
    def __init__(self, itemname: str, creator: User, amount: int, tags: dict, initial_value: float):
        self.initial_value = initial_value
        self.name = itemname
        self.creator = creator
        self.amount = amount
        self.owners = []
        self.token = "T_" + bcrypt.kdf(base64.b64encode(str(random.choices(chars, k=32)).encode()), bcrypt.gensalt(),
                                       32, 32).hex()
        self.tags = tags

    def mint_item(self):
        pass
        #TODO mint items

    def item_has_tag(self, tag: str):
        for i in self.tags.keys():
            if i == tag:
                return True
        else:
            return False

    def is_item_owner(self, user: User):
        for i in self.owners:
            if i==user:
                return True
        else:
            return False

    def drop_item(self, owner: User):
        if self.is_item_owner(owner):
            self.amount-=1
            u = self.owners[self.owners.index(owner)]
            u.wallet.accept_income(u.wallet.hash, u.wallet.currency.dollar_to_coin(self.initial_value))
            self.owners.remove(u)
            return True
        return False
