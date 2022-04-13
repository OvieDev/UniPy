from Currency import Currency
from Database import Database
from Session import Session
from Miner import Miner
from User import User
import datetime


db = Database()
admin = User(True, db.wallets[0], "admin", db)
admin.cmd_input()
