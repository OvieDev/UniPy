events = {
    "on_command": [],
    "on_payed": []
}


def subscribe_to_event(name: str = "", *args, **kwargs):
    def inner(func):
        for k in events.keys():
            if k == name:
                function_dict = {"event_args": kwargs, "function": lambda: func(kwargs, args)}
                events.get(k).append(function_dict)
                break
        else:
            raise AttributeError("Unknown event")

    return inner


def call_event(name: str, **kwargs):
    for i in events.get(name):
        try:
            should = True
            for k, v in enumerate(i["event_args"].keys()):
                req = False
                if v[:1] == "_":
                    req = True
                if req:
                    if not v == list(kwargs.keys())[k]:
                        should = False
                    else:
                        if not i["event_args"][v] == list(kwargs.values())[k]:
                            should = False
            if should:
                i["function"]()
            else:
                raise TypeError
        except TypeError:
            pass
            # yes i understand that's nooby, but it works ok


