class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_Node = Node(value)
        if self.head == None:
            self.head = new_Node
            self.tail = self.head
        else:
            self.tail.next = new_Node
            self.tail = new_Node

    def prepend(self, value):
        new_Node = Node(value)
        new_Node.next = self.head
        self.head = new_Node

    def printList(self):
        currNode = self.head
        while currNode != None:
            print(currNode.data,end=' --> ')
            currNode = currNode.next

    def deleteDups(self):
        duplicates = {}
        currNode = self.head
        prev = None
        while currNode != None:
            if currNode.data in duplicates.keys():
                prev.next = currNode.next
            else:
                duplicates[currNode.data] = 1
                prev = currNode
            currNode = currNode.next

    def noBufferDeleteDups(self):
        currNode = self.head
        while currNode != None:
            runner = currNode
            while runner.next != None:
                if runner.next.data == currNode.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currNode = currNode.next


myLL = LinkedList()
myLL.append(10)
myLL.append(5)
myLL.append(16)
myLL.prepend(1)
myLL.append(1)
print(myLL.printList())
# myLL.deleteDups() # O(n)
myLL.noBufferDeleteDups() #O(n^2)
print(myLL.printList())