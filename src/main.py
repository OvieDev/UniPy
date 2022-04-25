from Database import Database

from User import User

db = Database()
admin = User(True, db.wallets[0], "admin", db)
user1 = User(False, db.wallets[1], "user1", db)
admin.cmd_input()
