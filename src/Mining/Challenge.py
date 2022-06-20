from enum import Enum
import random


class SessionType(Enum):
    SES_SCHOOL = 0
    SES_COMPUTE = 1
    SES_DEVELOP = 2


class Challenge:
    def __init__(self, miners_list, ses_type: SessionType, session):
        self.session = session
        self.miners_list = miners_list
        self.challenge_type = ses_type
        if ses_type is SessionType.SES_SCHOOL:
            self.teachers = random.choices(miners_list, k=6)
            self.questions = [1000000, 1000000, 1000000, 1000000, 1000000, 100000]

    def send_calculations(self):
        for i in self.miners_list:
            if i in self.teachers:
                continue
            else:
                found = False
                while not found:
                    pointer = random.randint(0, 5)
                    if self.questions[pointer] > 0:
                        found = True
                        success = i.calculate()
                        if success[0]:
                            i.wallet.accept_income(i.wallet.hash, self.session.rate)
                            self.questions[pointer] -= 1
                            self.teachers[pointer].wallet.accept_income(self.teachers[pointer].wallet.hash,
                                                                        self.session.rate)
                            self.session.db.emit_server_message("Mining with wallet: ")
                    else:
                        continue
