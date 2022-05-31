import datetime
import functools

from src.Commands.CmdArgument import CmdArgument
from src.Protocol import Protocol
from src.ProtocolException import ProtocolException


# Command flags
# Flag #0: Admin rights - You need admin permission to use this command
# Flag #1: Server mode - You need to be in server mode to use this command
# Flag #2: View requirement - True is user view, False is server view
#

class Command:
    def __init__(self, command_name: str, flags: list, user: Protocol, func, *args):
        self.command_name = command_name
        self.user = user
        self.command_flags = flags
        self.arguments = args
        self.command_function = func

    def invoke_command(self, args: list):
        try:
            n_arg_state = []
            for c, i in enumerate(args):
                ni = 0
                if self.arguments[c] == CmdArgument.INTEGER:
                    ni = int(i)
                elif self.arguments[c] == CmdArgument.STRING:
                    ni = str(i)
                elif self.arguments[c] == CmdArgument.FLOAT:
                    ni = float(i)
                elif self.arguments[c] == CmdArgument.BOOL:
                    ni = bool(i)
                elif self.arguments[c] == CmdArgument.STRING_ARGS:
                    l = []
                    for n, y in enumerate(args):
                        if n < c:
                            continue
                        else:
                            l.append(y)
                    ni = l
                    n_arg_state.append(ni)
                    break
                elif self.arguments[c] == CmdArgument.HOURDATE:
                    times = i.split("/")
                    print(times)
                    n_times = [0, 0, 1, 0, 0, 0]  # seconds, minutes, hours, days, months, years
                    for i in times:
                        if i[:1] == "S" and int(i[1:]) > 0:
                            n_times[0] = int(i[1:])

                        elif i[:1] == "M" and int(i[1:]) > 0:
                            n_times[1] = int(i[1:])

                        elif i[:1] == "H" and int(i[1:]) > 0:
                            n_times[2] = int(i[1:])

                        elif i[:1] == "D" and int(i[1:]) > 0:
                            n_times[3] = int(i[1:])

                        elif i[:1] == "O" and int(i[1:]) > 0:
                            n_times[4] = int(i[1:])

                        elif i[:1] == "Y" and int(i[1:]) > 0:
                            n_times[5] = int(i[1:])

                    if functools.reduce(lambda a, b: a + b, n_times) <= 0:
                        raise AttributeError("Invalid date formatting")

                    ni = datetime.datetime.combine(datetime.date(datetime.datetime.now().year + n_times[5],
                                                                 datetime.datetime.now().month + n_times[4],
                                                                 datetime.datetime.now().day + n_times[3]),
                                                   datetime.time(datetime.datetime.now().hour + n_times[2],
                                                                 datetime.datetime.now().minute + n_times[1],
                                                                 datetime.datetime.now().second + n_times[0]))

                n_arg_state.append(ni)

            args = n_arg_state

            if self.command_flags[0] is True and not self.user.signer.is_admin:
                raise ProtocolException(self.user, "You do not have permission to use this command")

            if self.command_flags[1] is True and self.user.signer.view == 0:
                raise ProtocolException(self.user, "You're not in server view")

            if self.command_flags[2] is True and self.user.signer.view == 1 or self.command_flags[
                2] is False and self.user.signer.view == 0:
                raise ProtocolException(self.user, "You're in wrong view to use this command!")

            if len(args) != len(self.arguments):
                raise IndexError("Provided arguments number doesn't match with command arguments number")

            return self.command_function(args, self.user)

        except Exception as e:
            print("Exception while doing command")
            print(e)
