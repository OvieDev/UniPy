import math
import random
import time


class Miner:
    def __init__(self, db, minername, walletid, session, mode: int, *args):
        self.name = minername
        self.wallet = walletid
        self.sessionid = session
        self.nodes = args
        self.db = db
        self.mode = mode
        print("Initialized miner! "+minername+" running on sessionid: "+session.name)
        print("Current "+walletid.currency.name+" rate: "+session.rate)
        cont = input("Do you want to continue with your current session? [y/n]")
        if cont=="y":
            print("Great! Your session should be running now!")
        else:
            del self

    def connect_to_session(self):
        if len(self.sessionid.miners)<60:
            print("Connecting to session...")
            print("Checking wallet validity...")
            if self.db.wallets.count(self.wallet) != 0:
                self.sessionid.miners.append(self)
            else:
                print("Wallet validity check failed (is your walletID right?)")

    def calculate(self):
        success = False
        try:
            start = time.time()
            for i in range(1000):
                i+=5
                i=math.sqrt(i)*50
                i=math.cos(math.sqrt(i)*math.sin(5)*math.pi)/math.pi
            endloop = time.time()
            rnum = random.randint(0,100000000)
            found = True
            while(found):
                if random.randint(0,100000000)==rnum:
                    found=False
            endrandom = time.time()
            success=True
        except Exception as e:
            print("Couldn't finish process")
            return success
        return success, start-endloop, endloop-endrandom