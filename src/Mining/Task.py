import asyncio

from TaskType import TaskType, SessionType
from src import User


class Task:
    def __init__(self, t_type: TaskType, ses_type: SessionType, json: str, task_creator: User.User, funds: float):
        self.task_type = t_type
        self.session_type = ses_type
        self.json_code = json
        self.creator = task_creator
        self.funds = funds
        self.assigned_miners = []

    def runTask(self):
        asyncio.run(self.__taskRun())

    async def __taskRun(self):
        for i in self.assigned_miners:
            dat = await i.returnTaskResult()

