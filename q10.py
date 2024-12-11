class Pilha:
    def __init__(self):
        self.itens = []

    def is_empty(self):
        return len(self.itens) == 0

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        if not self.is_empty():
            return self.itens.pop()
        else:
            return "A pilha está vazia"

    def peek(self):
        if not self.is_empty():
            return self.itens[-1]
        else:
            return "A pilha está vazia"

    def size(self):
        return len(self.itens)
    
    def clear(self):
        self.itens = []

    def display(self):
        print("Pilha:", self.itens)

class Navegador:
    def __init__(self):
        self.pilha_voltar = Pilha()
        self.pilha_avancar = Pilha()
    
    def visitar_pagina(self, url):
        if not self.pilha_avancar.is_empty():
            self.pilha_avancar.clear()
        self.pilha_voltar.push(url)
        print(f"Visitando {url}")

    def voltar(self):
        if self.pilha_voltar.size()>1:
            url = self.pilha_voltar.pop()
            self.pilha_avancar.push(url)
            print(f"Voltando para {self.pilha_voltar.peek()}")
        else:
            print("Não há páginas para voltar.")

    def avancar(self):
        if not self.pilha_avancar.is_empty():
            url = self.pilha_avancar.pop()
            self.pilha_voltar.push(url)
            print(f"Avançando para {url}")
        else:
            print("Não há páginas para avançar.")


navegador = Navegador()

navegador.visitar_pagina("pagina1.com")
navegador.visitar_pagina("pagina2.com")
navegador.visitar_pagina("pagina3.com")
navegador.voltar()
navegador.voltar()
navegador.avancar()
navegador.voltar()
navegador.visitar_pagina("pagina4.com")
navegador.avancar()

