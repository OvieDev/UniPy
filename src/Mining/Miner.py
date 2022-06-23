import json
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

    async def returnTaskResult(self, sent_task: str):
        try:
            code = json.loads(sent_task)
            calls = code["function-main"]["calls"]
            identifiers = {}
            for index, element in enumerate(calls):
                if "identifier" in element:
                    identifiers[f"{element['identifier']}-main"] = [
                        element["type"],
                        element["value"],
                        element["modifiers"]
                    ]
                elif "operation" in element:
                    if element["operation"]=="out":
                        print(element["operand"])
                    elif element["operation"]=="in":
                        a = input()
                        identifiers[f"{element['operand']}-main"][2] = a
        except Exception as e:
            print("exception while executing ")
            print(e)

