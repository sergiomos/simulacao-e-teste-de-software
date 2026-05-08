class Estoque:
    """Controle simples de quantidades de produtos por nome."""

    def __init__(self):
        self._produtos = {}

    # --- REFACTOR ---
    # Centraliza a validacao de quantidade positiva em um helper unico,
    # eliminando duplicacao entre adicionar_produto e remover_produto.
    @staticmethod
    def _exigir_quantidade_positiva(quantidade):
        if quantidade <= 0:
            raise ValueError("quantidade deve ser positiva")

    def adicionar_produto(self, nome, quantidade):
        self._exigir_quantidade_positiva(quantidade)
        self._produtos[nome] = self._produtos.get(nome, 0) + quantidade

    def remover_produto(self, nome, quantidade):
        self._exigir_quantidade_positiva(quantidade)
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
