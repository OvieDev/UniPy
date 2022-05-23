events = {
    "on_command": [],
    "on_payed": []
}


def subscribe_to_event(name: str = "", *args, **kwargs):
    def inner(func):
        for k in events.keys():
            if k == name:
                function_dict = {"event_args": kwargs, "funciton": lambda: func(args)}
                events.get(k).append(function_dict)
                break
        else:
            raise AttributeError("Unknown event")

    return inner


def call_event(name: str, **kwargs):
    for i in events.get(name):
        try:
            i["funciton"]()
        except TypeError:
            pass
            # yes i understand that's nooby, but it works ok

