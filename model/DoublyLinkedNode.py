class DoublyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class BuildNode:
    def __init__(self, numbers):
        tail_node_l = None
        doubly_linked_list = None
        # Iterate through the list, converting each element into a doubly linked list node and adding it to the list
        for number in numbers:
            # Create a doubly linked list node
            node = DoublyLinkedNode(number)

            # If the list is empty, set the node as the head of the list
            if not doubly_linked_list:
                doubly_linked_list = node

            # Otherwise, add the node to the end of the list
            else:
                # Find the end of the list
                current_node = doubly_linked_list
                while current_node.next:
                    current_node = current_node.next

                # Add the node to the end of the list
                current_node.next = node
                node.prev = current_node
                tail_node_l = current_node.next

        head_node = doubly_linked_list
        tail_node = tail_node_l

        head_node.prev = tail_node
        tail_node.next = head_node
        self.data_node = doubly_linked_list
        self.size = len(numbers)

    def get_trunk_node(self, trunk, num):
        current_node = self.data_node
        while current_node.next:
            data = current_node.__getattribute__('data')
            if data == trunk:
                i = 1
                while current_node.prev:
                    if i == num:
                        return current_node.data
                    else:
                        i = i + 1
                        current_node = current_node.prev

            current_node = current_node.next

    def get_branch_node(self, trunk, num):
        current_node = self.data_node
        while current_node.next:
            data = current_node.__getattribute__('data')
            if data == trunk:
                i = 1
                while current_node.prev:
                    if i == num:
                        return current_node.data
                    else:
                        i = i + 1
                        current_node = current_node.prev
            current_node = current_node.next
