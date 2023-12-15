# Ex: Graphs

class Node:
    # constructor
    def __init__(self, value, next):
        self.value = value
        self.next = next


# a linked list is a list of nodes
class LinkedList:
    def __init__(self):
        self.value = None
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

    def deleteValue(self, value):  # O(n+n)=O(n), n being the number of elements in my list
        elements = []
        while self.size > 0:  # I have remaining elements in my list, O(n)
            temp = self.deleteHead()  # remove a node #O(1)
            if temp != value:  # check the value I removed, if it is not the one I want to delete , add it to elements
                elements.append(value)
        for i in elements:  # add back the elements to my LL, O(n)
            self.addAtHead(i)  # O(1)


class AdjacencyList:
    def __init__(self, V):
        self.v = V
        self.list_LL = []
        for i in range(V):
            self.list_LL.append(LinkedList())

    def addEdge(self, city1, city2):  # O(V)
        if not city1.search(city2.value):  # O(V), v being the number of vertices
            city1.addAtHead(city2.value)

    def deleteEdge(self, vs, ve):  # O(V)
        if self.list_LL[vs].search(ve):
            self.list_LL[vs].deleteValue(ve)

    def showGraph(self):
        for i in range(len(self.list_LL)):
            print("(", self.list_LL[i].value, ")", end="")
            self.list_LL[i].printLL()

    def getVerticesInCommon(self, v1, v2):  # O(V^2)
        V = len(self.list_LL)
        for i in range(V):  # O(V)
            if self.list_LL[v1].search(i) is True and self.list_LL[v2].search(i):  # O(V)
                print(i, end=" ")
        print()

    def checkCities(self, city1, city2):
        if city1.size == 0:
            return False
        else:
            current = city1.head
            while current is not None:
                if current.value == city2.value:
                    return True
                current = current.next
        if city2.size == 0:
            return False
        else:
            current = city2.head
            while current is not None:
                if current.value == city1.value:
                    return True
                current = current.next
        return False

    def checkRoutes(self, city1):
        if city1.size == 0:
            return None
        current = city1.head
        while current is not None:
            print(current.value, ",", end=" ")
            current = current.next
        print()

    def isCyclic(self):
        visited = [False] * self.v
        helper = [False] * self.v
        for i in range(self.v):
            if not visited[i]:
                ans = self.DFS(i, visited, helper)
                if ans:
                    return True
        return False

    def DFS(self, i, visited, helper):
        visited[i] = True
        helper[i] = True
        neighbours = []
        current = self.list_LL[i].head
        while current is not None:
            neighbours.append(current)
            current = current.next
        for k in range(len(neighbours)):
            if helper[k]:
                return True
            if not visited[current.value]:
                ans = self.DFS(current.value, visited, helper)
                if ans:
                    return True
            current = current.next
        helper[i] = False
        return False


g2 = AdjacencyList(4)
Beirut = g2.list_LL[0]
Beirut.value = "Beirut"
Saida = g2.list_LL[1]
Saida.value = "Saida"
Byblos = g2.list_LL[2]
Byblos.value = "Byblos"
Tyre = g2.list_LL[3]
Tyre.value = "Tyre"
g2.addEdge(Byblos, Beirut)
g2.addEdge(Beirut, Byblos)
g2.addEdge(Beirut, Saida)
g2.addEdge(Saida, Tyre)
g2.addEdge(Saida, Beirut)
g2.addEdge(Tyre, Saida)
if g2.checkCities(Beirut, Byblos):
    print("There is a rout")
g2.checkRoutes(Beirut)
g2.showGraph()

if g2.isCyclic():
    print("Cyclic")
else:
    print("None cyclic")
