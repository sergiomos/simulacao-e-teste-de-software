class Estoque:
    def __init__(self):
        self._produtos = {}

    # --- GREEN ---
    # Implementacao minima para o teste passar.
    def adicionar_produto(self, nome, quantidade):
        self._produtos[nome] = quantidade

    def consultar_quantidade(self, nome):
        return self._produtos.get(nome, 0)
