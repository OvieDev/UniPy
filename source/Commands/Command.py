from source.Commands.CmdArgument import CmdArgument
from source.Protocol import Protocol
from source.ProtocolException import ProtocolException


class Command:
    def __init__(self, command_name: str, flags: list, user: Protocol, func, *args):
        self.command_name = command_name
        self.user = user
        self.command_flags = flags
        self.arguments = args
        self.command_function = func

    def invoke_command(self, args: list):
        try:
            if self.command_flags[0] is True and not self.user.signer.is_admin:
                raise ProtocolException(self.user, "")
            if len(args) != len(self.arguments):
                raise IndexError("Provided arguments number doesn't match with command arguments number")

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
                args[c] = ni
            self.command_function(args)

        except Exception as e:
            print("Exception while doing command")
            print(e)
