from Currency import Currency
from Database import Database
from Session import Session
from Miner import Miner
import datetime

from User import User

db = Database()
admin = User(True, db.wallets[0], "admin", db)
admin.cmd_input()
