class MultiStack:
    def __init__(self, stackSize):
        self.numberofStacks = 3
        self.values = [0] * (stackSize * self.numberofStacks)
        self.sizes = [0] * self.numberofStacks
        self.stackCapacity = stackSize

    # Push value onto stack
    def push(self, stackNum, value):
        # Check if we have space for next element
        if self.isFull(stackNum):
            raise Exception('Stack is Full')
        self.sizes[stackNum] += 1 # Increment stack pointer
        self.values[self.indexOfTop(stackNum)] = value # Update the top value

    # Pop item from top of the stack
    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is Empty')
        value = self.values[self.indexOfTop(stackNum)] # Get top
        self.values[self.indexOfTop(stackNum)] = 0 # Clear
        self.sizes[stackNum] -= 1 # Shrink
        return value

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is Empty')
        return self.values[self.indexOfTop(stackNum)]

    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.stackCapacity

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackCapacity
        return offset + self.sizes[stackNum] - 1

    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0

newStack = MultiStack(3)
newStack.push(0,20)
newStack.push(0,9)
newStack.push(1,90)
newStack.push(1,70)
newStack.push(2,100)
print(newStack.peek(2))
print(newStack.peek(1))
print(newStack.pop(1))
print(newStack.peek(1))