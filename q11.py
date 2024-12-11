class Fila:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        return self.itens.pop(0)

    def peek(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        return self.itens[0]

    def size(self):
        return len(self.itens)

    def display(self):
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:", end=" ")
            for item in self.itens:
                print(item, end=" ")
            print()


fila_atendimento = Fila()

fila_atendimento.enqueue("Chamado 1")
fila_atendimento.enqueue("Chamado 2")
fila_atendimento.enqueue("Chamado 3")

print("--- Chamados na fila ---")
fila_atendimento.display()

print("\nAtendendo:", fila_atendimento.dequeue())

print("\n--- Chamados na fila ---")
fila_atendimento.display()

print("\nAtendendo:", fila_atendimento.dequeue())

print("\n--- Chamados na fila ---")
fila_atendimento.display()

print("\nPróximo chamado a ser atendido:", fila_atendimento.peek())
print("\nQuantidade de chamados na fila:", fila_atendimento.size())