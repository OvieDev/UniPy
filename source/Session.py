class Session:
    def __init__(self, sesid, currency, rate, db, hidden=False):
        self.id = sesid
        self.coin = currency
        self.rate = rate
        self.miners = []
        self.hidden = hidden
        self.db = db
        db.emit_server_message("Initialized session for "+self.coin.name+"!")
        if self.hidden:
            db.emit_server_message("ID: "+sesid)
        else:
            print("ID: "+sesid)


    def challenge_init(self):
        print("Session begun!")
