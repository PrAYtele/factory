class MyQueue:

    def __init__(self):

        self.stackin = []
        self.stackout = []

    def push(self, x: int) -> None:

        self.stackin.append(x)

    def pop(self) -> int:

        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout.pop()

    def peek(self) -> int:

        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout[-1]

    def empty(self) -> bool:

        if not self.stackin and not self.stackout:
            return True
        else:
            return False