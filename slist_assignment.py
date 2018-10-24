class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SList:
    def __init__(self,value):
        node = Node(value)
        self.head = node

    def addNode(self,value):
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        node = Node(value)
        runner.next = node

    def printAllValues(self):
        runner = self.head
        while (runner.next != None):
            print(runner.value)
            runner = runner.next
        print(runner.value)

    def removeNode(self,value):
        runner = self.head
        if runner.value == value:
            self.head = runner.next
        while(runner.next != None):
            current_node = runner
            runner = runner.next
            if runner.value == value:
                current_node.next = runner.next
            if runner.value == value and runner.next == None:
                runner.next = current_node
                runner = runner.next



list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.removeNode(9) # removes 9, which is one of the middle nodes in the list
list.removeNode(5) # removes 5, which is the first value in the list
list.removeNode(1) # removes 1, which is the last node in the list
list.printAllValues()