class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if type(val)==int:
            self.stack.append(val)
            min_val = min(val,self.min_stack[-1] if self.min_stack else val)
            self.min_stack.append(min_val)
        else:
            self.stack.append(None)
            self.min_stack.append(None)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
