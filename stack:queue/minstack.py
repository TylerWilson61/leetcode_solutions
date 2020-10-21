class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.stack == []:
            self.min.append(x)
            
        if x <= self.min[-1]:
            self.min.append(x)
            
        self.stack.append(x)
        return 

    def pop(self):
        """
        :rtype: None
        """
        dlt = self.stack.pop()
        if dlt == self.min[-1]:
            self.min.pop()
        return
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
