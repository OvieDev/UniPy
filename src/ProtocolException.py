class ProtocolException(Exception):
    def __init__(self, proto, errmes):
        self.protocol = proto
        self.message = errmes

    def __repr__(self):
        return f"Protocol based exception from protocol {self.protocol.name} with id {self.protocol.id}.\n Message: {self.message}"
