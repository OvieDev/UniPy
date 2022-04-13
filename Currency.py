class Currency:
    def __init__(self, name, author, info, amount, dp):
        self.name = name
        self.author = author
        self.info = info
        self.dollar_price = dp

    def info(self):
        print("COIN: "+self.name+" by "+self.author+" "+self.info)