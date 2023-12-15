Ex: 4
class Node:
    # constructor
    def __init__(self, value, next):
        self.value = value
        self.next = next


# a linked list is a list of nodes
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # the number of nodes in the LL

    def addAtHead(self, value):  # O(1)
        n = Node(value, None)
        if self.size == 0:  # LL is empty
            self.head = n
            self.tail = n
            self.size = 1
        else:  # LL is not empty
            n.next = self.head
            self.head = n
            self.size += 1

    def addAtTail(self, value):  # O(1)
        n = Node(value, None)
        if self.size == 0:  # LL is empty
            self.head = n
            self.tail = n
            self.size = 1
        else:
            self.tail.next = n
            self.tail = n
            self.size += 1

    def search(self, info):  # O(n), n being the length of the list
        if self.size == 0:
            return False  # LL is empty

        current = self.head  # current keeps track of the node I am at

        while current is not None:  # O(n)
            if current.value == info:
                return True
            else:
                current = current.next
        return False

    def deleteHead(self):  # O(1)
        if self.size == 0:  # O(1)
            return None  # O(1)
        elif self.size == 1:  # O(1)
            temp = self.head.value  # O(1)
            self.head = None  # O(1)
            self.tail = None  # O(1)
            self.size = 0  # O(1)
            return temp  # O(1)
        # we have more than one node
        else:
            temp = self.head.value  # O(1)
            self.head = self.head.next  # O(1)
            self.size -= 1
            return temp  # O(1)

    def deleteTail(self):  # O(n), n being the size of the LL
        if self.size <= 1:  # size == 0 or size ==1
            return self.deleteHead()

        # size>=2
        current = self.head
        temp = self.tail.value
        # while current.next!=self.tail: #O(n)
        while current.next.next is not None:
            current = current.next

        current.next = None
        self.tail = current
        self.size -= 1
        return temp

    def printLL(self):
        if self.size == 0:
            print("my LL is empty")
        current = self.head
        while current is not None:
            print(current.value, "->", end=" ")
            current = current.next
        print()

    def deleteAtIndex(self, index):
        if self.size == 0:
            return
        elif index == 0:
            self.deleteHead()
        elif index == self.size - 1:
            self.deleteTail()
        elif 0 > index or self.size <= index:
            print("index out of range")
            return
        else:
            count = 0
            current = self.head
            while count < index-1:
                current = current.next
                count += 1
            current.next = current.next.next


ll = LinkedList()
ll.printLL()
ll.addAtHead(76)
ll.addAtHead(56)
ll.addAtTail(11)
ll.addAtTail(0)
ll.addAtHead(12)
ll.printLL()
ll.deleteAtIndex(3)
ll.printLL()
