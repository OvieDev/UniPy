events = {
}


def subscribe_to_event(name: str = ""):
    def inner(func):
        for k, v in events.items():
            if k==name:
                v.append(func)
                break
        else:
            raise AttributeError("Unknown event")
    return inner


def call_event(name: str):
    for i in events.get(name):
        i()
