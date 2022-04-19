import os


def help_command(arg):
    print("""
                 USER COMMANNDS:
                  - ses_create: Creates session for default wallet currency for 30$
                  - transactions: Preview all your transactions
                  - server_console (ADMIN-ONLY): Goes to the server
                  - cls (SERVER AND USER): Clears console
    
                 SERVER COMMANDS (ADMIN-ONLY):
                  - user_mode: Goes back to user view
                 """)


def clear_command(arg):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Cleared!")


def ses_create_command(arg):
    if len(arg[0]) != 3:
        raise IndexError("Currency name too short or too long (must be 3 characters long)")
    print("Session created")