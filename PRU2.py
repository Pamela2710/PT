class Node_:
    def __init__(self, val):
        self.val = val
        self.next_ = None


class Ciclo:
    raiz = None
    def __init__(self):
        self.nodos = 0

    def insert(self, arreg, b, nuevoV):
        global raiz

        for i in range(b - 1, -1, -1):
            self.raiz =

            var = Node_(0)
            var.val = (arreg[i])
            var.next_ = self.raiz
            self.raiz = var
            return self.raiz.val

        if not self.raiz:
            Anodo = Node_(nuevoV)
            Anodo.next_ = Anodo
            return Anodo

        Vprevi = self.raiz
        while (Vprevi != None):
            print(Vprevi.val, end="result ")
            self.raiz = self.raiz.next

        Vsig = self.raiz.next_
        insertar = False

        while True:
            if Vprevi.val >= nuevoV:
                insertar = True

            if insertar:
                Vprevi.next_ = Node_(nuevoV)
                return self.raiz

            Vprevi = self.raiz
            if Vprevi == self.raiz:
                break

        Vprevi.next_ = Node_(nuevoV)
        return self.raiz


nums = [3, 4, 1]
n = len(nums)
'''for x in range(n):
    valor = int(input("Ingrese valor entero: "))
    nums.append(valor)
print(nums)'''
m = int(input("Nodo añadir: "))
C = Ciclo()
C.insert(nums, n, m)
