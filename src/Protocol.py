from ProtocolException import ProtocolException
import datetime

import Database
import User


class Protocol:
    def __init__(self, signer: User, identify: int, time: datetime.datetime, db: Database, name="DProt"):
        self.database = db
        self.signer = signer
        self.id = identify
        self.name = name
        self.time = time
        self.valid = True

    def run_protocol(self):
        try:
            self.database.emit_server_message("Test Protocol sent message")
        except ProtocolException as e:
            print(e)
            self.valid = False
        self.database.proto_archive.append({
            "protocol_id": self.id,
            "protocol_name": self.name,
            "protocol_signtime": self.time,
            "protocol_signer": self.signer.public_key_name,
            "success": self.valid,
            "details": [
                "Test Protocol"
            ]
        })
