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
            if self.command_flags[0] is True and not self.user.signer.is_admin:
                raise ProtocolException(self.user, "You do not have permission to use this command")
            if self.command_flags[1] is True and self.user.signer.view==0:
                raise ProtocolException(self.user, "You're not in server view")
            if self.command_flags[2] is True and self.user.signer.view==1 or self.command_flags[2] is False and self.user.signer.view==0:
                raise ProtocolException(self.user, "You're in wrong view to use this command!")
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
            self.command_function(args, self.user)

        except Exception as e:
            print("Exception while doing command")
            print(e)
