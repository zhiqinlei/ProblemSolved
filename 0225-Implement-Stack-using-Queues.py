class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        self.Top = None # cannot use top
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q2.append(x)
        self.Top = x
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q2, self.q1 = self.q1, self.q2

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        ans = self.q1.popleft()
        if self.q1: # check q1
            self.Top = self.q1[0]
        return ans
        

    def top(self) -> int:
        """
        Get the top element.
        """
        
        return self.Top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.q1:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
