from Currency import Currency


class Wallet:
    def __init__(self, currency, hash, amount, name):
        self.currency = currency
        self.amount = amount
        self.__transactions = []
        self.name = name
        self.hash = hash

    def pay_and_return_value(self, amount):
        if self.amount - amount < 0:
            print("Cannot proceed payment. Amount too high to be extracted from wallet")
            return 0
        else:
            print(f"Payment completed successfully! Amount left: {self.amount - amount}")
            self.amount -= amount
            self.__transactions.append(f"PAY/{amount}")
            return amount

    def pay_with_dollars(self, dollar_val):
        amount = dollar_val / self.currency.dollar_price
        if self.amount - amount < 0:
            print("Cannot proceed payment. Amount too high to be extracted from wallet")
            return 0
        else:
            print(f"Payment completed successfully! Amount left: {self.amount - amount}")
            self.amount -= amount
            self.__transactions.append(f"PAY/{amount}")
            return amount

    def transactions(self):
        print("TRANSACTIONS MADE WITH THIS WALLET:")
        for i in self.__transactions:
            print(" - " + i)

    def accept_income(self, key, amount):
        if key == self.hash:
            self.amount += amount

    def wallet_info(self):
        walln = ""
        for i in self.name:
            walln += "*"
        return f"""Wallet:
        
        Currency: {self.currency.name}
        Amount: {self.amount}
        HashLock: {walln} 
        Wallet Name: {self.name}
        
                """

    def convert_from_currency(self, currency: Currency, amount: float):
        extern_coin_val = currency.coin_to_dollar(amount)
        coin_amount = self.currency.dollar_to_coin(extern_coin_val)
        self.currency.add_to_stash(coin_amount * 0.01)
        return currency.dollar_to_coin(self.currency.coin_to_dollar(coin_amount * 0.99))
