class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def __str__(self):
        return "{self.data}"

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtBegin(self, data):
        #create new node
        node = Node(data)

        #check for enty case
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

            