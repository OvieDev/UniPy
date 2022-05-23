events = {
    "on_command": [],
    "on_payed": []
}


def subscribe_to_event(name: str = "", *args):
    def inner(func):
        for k in events.keys():
            if k == name:
                events.get(k).append(func(args))
                break
        else:
            raise AttributeError("Unknown event")

    return inner


def call_event(name: str):
    for i in events.get(name):
        try:
            i()
        except TypeError:
            pass
            # yes i understand that's nooby, but it works ok

