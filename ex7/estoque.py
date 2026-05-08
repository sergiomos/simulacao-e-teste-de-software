class Estoque:
    def __init__(self):
        self._produtos = {}

    # --- GREEN ---
    # Quantidade > 0 obrigatoria; produto existente incrementa.
    def adicionar_produto(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("quantidade deve ser positiva")
        self._produtos[nome] = self._produtos.get(nome, 0) + quantidade

    def consultar_quantidade(self, nome):
        return self._produtos.get(nome, 0)
