import json


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

    async def returnTaskResult(self, sent_task: str):
        return sent_task
