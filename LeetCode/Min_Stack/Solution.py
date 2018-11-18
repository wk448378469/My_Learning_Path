class Pair(object):
    def __init__(self, key, currentMinValue):
        self.key = key
        self.currentMinValue = currentMinValue


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.n = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.n == 0 or x <= self.stack[-1].currentMinValue:
            self.stack.append(Pair(x, x))
        else:
            self.stack.append(Pair(x, self.stack[-1].currentMinValue))
        self.n += 1

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.n -= 1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1].key

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1].currentMinValue


if __name__ == '__main__':
    m = MinStack()
    m.push(-10)
    m.push(14)
    print(m.getMin())
    print(m.getMin())
    m.push(-20)
    print(m.getMin())
    print(m.getMin())
    print(m.top())
    print(m.getMin())
    m.pop()
    m.push(10)
    m.push(-7)
    print(m.getMin())
    m.push(-7)
    m.pop()
    m.pop()
    print(m.getMin())
    m.pop()
