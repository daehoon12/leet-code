class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        
        if not self.min_st or self.min_st and self.min_st[-1] >= val:
            self.min_st.append(val)

    def pop(self) -> None:

        poped = self.st.pop()
        if self.min_st and self.min_st[-1] == poped:
            self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()