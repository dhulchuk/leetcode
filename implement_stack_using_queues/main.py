#  stack design
from queue import Queue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for x in range(self.queue.qsize() - 1):
            self.queue.put(self.queue.get())
        return self.queue.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        element = self.pop()
        self.push(element)
        return element

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()