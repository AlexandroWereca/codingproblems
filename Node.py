class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.rigth_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = Node(value)
        else:
            new_node = Node(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_rigth(self, value):
        if self.rigth_child == None:
            self.rigth_child = Node(value)
        else:
            new_node = Node(value)
            new_node.rigth_child = self.rigth_child
            self.rigth_child = new_node