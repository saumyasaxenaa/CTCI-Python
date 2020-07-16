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
            print(currNode.data, end=' --> ')
            currNode = currNode.next

    def printKthtoLast(self, K):
        p1, p2 = self.head, self.head
        for i in range(K):
            if p1 == None:
                return None
            p1 = p1.next
        while p1 != None:
            p1 = p1.next
            p2 = p2.next
        return p2.data

myLL = LinkedList()
myLL.append(11)
myLL.append(40)
myLL.append(8)
myLL.prepend(90)
print(myLL.printList())
print(myLL.printKthtoLast(2))

