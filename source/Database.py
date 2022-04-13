import string
import threading
import random
import time

from Currency import Currency
import Session
import sys


from Wallet import Wallet

sys.setrecursionlimit(10000)


class Database:
    def __init__(self):
        print("Database initializing. Please wait...")
        self.currencies = [Currency("PythonCash","ComputeLabs","\nThis is basic coin initialized every time!", 500, 13000)]
        self.wallets = [Wallet(self.currencies[0],"abcdefg",10000,"ADMIN_WALLET")]
        self.running_sessions = []
        self.log = []

        def create_session():
            while True:
                if random.randint(10, 100) == 10:
                    self.add_session(random.choice(self.currencies), hidden=True)
                time.sleep(2)
        print("DB initialized!\nAll currencies,wallets and sessions have been loaded")
        self.ses_t = threading.Thread(target=create_session)
        self.ses_t.start()

    def add_session(self, currency, hidden=False):
        self.running_sessions.append(Session.Session(
            ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(40)),
            currency, random.uniform(0.0001, 0.1), self, hidden=hidden))
        self.emit_server_message("[DB] Session for "+currency.name+" started!")

    def emit_server_message(self, msg):
        self.log.append(msg)
