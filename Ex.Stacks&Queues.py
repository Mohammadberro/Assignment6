Ex: 1


class Stack:
    def __init__(self):
        self.items = []

    # return True if the stack is empty
    def isEmpty(self):  # O(1)
        if len(self.items) == 0:
            return True
        else:
            return False

    # adds an item to the stack
    # params: value, item to add
    def push(self, value):  # O(1)
        self.items.append(value)

    # returns the value deleted from the stack
    def pop(self):  # O(1)
        if self.isEmpty():
            return None
        return self.items.pop()

    def checkPalindrome(self, word):
        temp = []
        for char in word:
            self.items.append(char)
        while self.items:
            temp.append(self.pop())
        reversed_word = ''.join(map(str, temp))
        if reversed_word == word:
            return True


MyStack = Stack()

word = input("Enter a word")
if MyStack.checkPalindrome(word):
    print("Palindrome")
else:
    print("Non Palindrome")

Ex: 2


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

    def isEmpty(self):
        return self.size == 0

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


class Queue:
    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, value):  # O(1)
        self.items.addAtTail(value)  # O(1)

    def dequeue(self):  # O(1)
        if self.items.isEmpty():
            return None
        return self.items.deleteHead()


def checkBalanced(expression):
    opening_symbols = ["(", "[", "{"]  # Creating Lists to point matching symbols
    closing_symbols = [")", "]", "}"]
    for x in expression:
        if x in opening_symbols:  # Adding Opening symbols to my stack
            MyStack.push(x)
        elif x in closing_symbols:
            '''' Criteria: fist closing symbol should match the last opening symbol (at the point of looping),
            so the closing symbol will be queued'''
            MyQueue.enqueue(x)
            if closing_symbols.index(MyQueue.dequeue()) != opening_symbols.index(MyStack.pop()):
                return False
    if MyStack.isEmpty():
        return True


MyQueue = Queue()
MyStack = Stack()
expression = input("Enter an Expression")
if checkBalanced(expression):
    print("Balanced")
else:
    print("Unbalanced")
