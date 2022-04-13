from ProtocolException import ProtocolException
import datetime


class Protocol:
    def __init__(self, signer: str, identify: int, time: datetime.datetime, name="DProt"):
        self.signer = signer
        self.id = identify
        self.name = name
        self.time = time
        self.valid = True

    def run_protocol(self):
        try:
            pass
        except ProtocolException as e:
            pass