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
            if datetime.datetime.now() > self.date_end:
                raise ProtocolException(self, "Protocol Expired")
            else:
                self.proto_code()
        except ProtocolException as e:
            print(e)

    def proto_code(self):
        pass