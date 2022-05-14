from src.Commands.CmdArgument import CmdArgument
from src.Commands.Command import Command
from src.Commands.CommandFunctions import *
from src.Database import Database
from src.Protocol import Protocol
from src.ProtocolException import ProtocolException
import src.User


class CommandSendProtocol(Protocol):
    def __init__(self, signer: src.User.User, identify: int, time: datetime, db: Database, command: str, *args, name="CommandSend",):
        super().__init__(signer, identify, time, db, name=name)
        self.commands = [Command("help", [False, False, None], self, help_command),
                         Command("cls", [False, False, None], self, clear_command),
                         Command("ses_create", [False, False, True], self, ses_create_command, CmdArgument.STRING),
                         Command("server_mode", [True, False, None], self, server_mode_move_command),
                         Command("pay", [False, False, True], self, pay_command, CmdArgument.STRING, CmdArgument.STRING_ARGS),
                         Command("client", [False, False, True], self, client_command)]
        self.command_sent = command
        if len(args)>0:
            self.arguments = list(args)[0]
        else:
            self.arguments = []

    def run_protocol(self):
        try:
            for i in self.commands:
                if self.command_sent == i.command_name:
                    return i.invoke_command(self.arguments)

            else:
                raise ProtocolException(self, "Unknown command")
        except ProtocolException as e:
            print(e)
