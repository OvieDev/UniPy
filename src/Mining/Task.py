import asyncio

from TaskType import TaskType, SessionType
from src import User


class Task:
    def __init__(self, t_type: TaskType, ses_type: SessionType, jar: str, task_creator: User.User, funds: float):
        self.task_type = t_type
        self.session_type = ses_type
        self.jar = open(f"{jar}.jar")
        self.creator = task_creator
        self.__max = funds
        self.funds = funds
        self.assigned_miners = []
        self.cut = 0.01
    def runTask(self):
        asyncio.run(self.__taskRun())

    async def __taskRun(self):
        for i in self.assigned_miners:
            dat = await i.returnTaskResult()
            if dat:
                i.wallet.accept_income(i.wallet.hash, self.funds-(self.__max*self.cut))
                self.funds -= (self.__max * self.cut)


