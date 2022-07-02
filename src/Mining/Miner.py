import json
import os

from MiningMode import MiningMode


class Miner:
    def __init__(self, db, minername, walletid, session, mode: MiningMode, *args):
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

    async def returnTaskResult(self, sent_task):
        try:
            os.system(f"java -jar {sent_task}.jar")
            return True
        except Exception as e:
            print("exception while executing ")
            print(e)
            return False

