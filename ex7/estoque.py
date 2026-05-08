class Estoque:
    def __init__(self):
        self._produtos = {}

    # --- GREEN ---
    # Quantidade > 0 obrigatoria; produto existente incrementa.
    def adicionar_produto(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("quantidade deve ser positiva")
        self._produtos[nome] = self._produtos.get(nome, 0) + quantidade

    def remover_produto(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("quantidade deve ser positiva")
        disponivel = self._produtos.get(nome, 0)
        if disponivel == 0:
            raise ValueError(f"produto '{nome}' nao existe no estoque")
        if quantidade > disponivel:
            raise ValueError("quantidade a remover maior que o disponivel")
        self._produtos[nome] = disponivel - quantidade

    def consultar_quantidade(self, nome):
        return self._produtos.get(nome, 0)

    def listar_produtos(self):
        return [nome for nome, qtd in self._produtos.items() if qtd > 0]

    def produto_mais_estocado(self):
        disponiveis = {n: q for n, q in self._produtos.items() if q > 0}
        if not disponiveis:
            return None
        return max(disponiveis, key=disponiveis.get)
