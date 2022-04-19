from Database import Database

from User import User

db = Database()
admin = User(True, db.wallets[0], "admin", db)
admin.cmd_input()
