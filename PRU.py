class Node:
    def __init__(self, data):
        self.data = data
        self.next = next


# Function to insert Node
def insert(root, item):
    #espacios de memoria 0008890#njfeu7
    temp = Node(0)
    #conversion nodos individuales
    temp.data = item
    #print(temp.data)
    #linkedL entero None a punteros temp valores arreglo q ya no es arr
    temp.next = root
    root = temp
    #return root
    print(root.data)

def display(root):
    while (root != None):
        print(root.data, end=" ")
        root = root.next

def arrayToList(arr, n):
    root = None
    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])
        print(root)
    return root

# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5];
    n = len(arr)
    root = arrayToList(arr, n);
    display(root)