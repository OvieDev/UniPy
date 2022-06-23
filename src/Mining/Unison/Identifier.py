from src.Mining.Unison.OperationType import OperationType


class Identifier:
    def __init__(self, scope: str, value: str, type: str, modifiers: int):
        self.scope = scope
        self.type = type
        if type == "int":
            self.value = int(value)
        elif type == "float":
            self.value = float(value)
        elif type == "bool":
            self.value = bool(value)
        elif type == "list":
            self.value = value.split(" ")
        elif type == "string":
            self.value = value
        self.modifiers = modifiers

    def operation(self, operation: OperationType, operand):
        if operation == OperationType.ASSIGN:
            if self.modifiers:
                raise Exception("Cannot assign to const value")
            self.value = operand
            return
        if operation == OperationType.ADD:
            return self.value + operand

        if operation == OperationType.SUB:
            return self.value - operand

        if operation == OperationType.MUL:
            return self.value * operand

        if operation == OperationType.DIV:
            return self.value / operand

        if operation == OperationType.ADDEQ:
            if self.modifiers:
                raise Exception("Cannot assign to const value")
            self.value += operand
            return

        if operation == OperationType.SUBEQ:
            if self.modifiers:
                raise Exception("Cannot assign to const value")
            self.value -= operand
            return

        if operation == OperationType.MULEQ:
            if self.modifiers:
                raise Exception("Cannot assign to const value")
            self.value *= operand
            return

        if operation == OperationType.DIVEQ:
            if self.modifiers:
                raise Exception("Cannot assign to const value")
            self.value /= operand
            return

        if operation == OperationType.EQUALS:
            return self.value == operand

        if operation == OperationType.NOT:
            return not self.value

        if operation == OperationType.AND:
            return self.value and operand

        if operation == OperationType.OR:
            return self.value or operand
