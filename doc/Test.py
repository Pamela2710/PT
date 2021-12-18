import time
def sum_n(n):
    start = time.time()
    total = 0
    for i in range(1, n + 1):
        total += i
    return time.time() - start


def reverse_str(string):
    if len(string) == 0:
        return
    temp = string[0]
    reverse_str(string[1:])
    print(temp, end='')




class Node:
    def __init__(self, val=None):
        self.val = val
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node

class Singly_linked_list:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert_end(self, val):
        node = self.head_node
        while node.next_node:
            node = node.next_node
        new_node = Node(val)
        node.next_node = new_node

    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node

    def swap(self, x):
        if not x:
            return

        else:
            node=x

        if not node or not node.next_node:
            return node

        first = node
        second = node.next_node
        first.next_node = self.swap(second.next_node)
        second.next_node = first
        if(node==self.head_node):
            self.head_node=second
        return second


a = Node('A')
L = Singly_linked_list(a)
L.insert_end('B')
L.insert_end('C')
L.insert_end('E')
L.insert_end('F')
L.insert_end('G')

L.swap(a)
L.list_traversed()
