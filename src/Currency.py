class Currency:
    def __init__(self, name, author, info, amount, dp):
        self.name = name
        self.author = author
        self.info = info
        self.dollar_price = dp
        self.__max_currency = amount
        self.__current_amount = amount*0.9
        self.__stash_amount = amount*0.1

    def info(self):
        print("COIN: "+self.name+" by "+self.author+" "+self.info)

    def add_to_stash(self, amount):
        self.__current_amount -= amount
        self.__stash_amount += amount

    def coin_to_dollar(self, coin_amount):
        return coin_amount*self.dollar_price

    def dollar_to_coin(self, dollar_amount):
        return dollar_amount/self.dollar_price
