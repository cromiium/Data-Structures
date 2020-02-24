class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        if self.is_empty():
            self.insert_head(data)
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = Node(data)

    def delete_head(self):
        if not self.is_empty():
            temp = self.head
            self.head = self.head.next
            temp.next = None

    def delete_node(self, data):
        if not self.is_empty():
            temp = self.head
            if temp.head.data == data:
                self.delete_head()
            else:
                while(temp.next):
                    if temp.data.next == data:
                        temp.next = temp.next.next
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def is_empty(self) -> bool:
        if self.head == None:
            return True
        else:
            return False

def main():
    list1 = LinkedList()
    for index in range(0,5):
        list1.insert_head(index)
    list1.print_list()
    list1.delete_head()
    list1.print_list()
    list1.delete_node(3)
    list1.print_list()
main()