class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end='->')
            temp = temp.next  
        print("None")

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(30)

    print("Linked List:")
    linked_list.display()