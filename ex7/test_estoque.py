import unittest

from estoque import Estoque


class TestAdicionarProduto(unittest.TestCase):
    # --- RED ---
    # Primeiro teste: ao adicionar um produto, a consulta deve refletir a quantidade.
    # Antes de implementar, este teste falha porque Estoque ainda nao existe.
    def test_adicionar_produto_novo(self):
        e = Estoque()
        e.adicionar_produto("caneta", 10)
        self.assertEqual(e.consultar_quantidade("caneta"), 10)

    # --- RED ---
    # Adicionar produto ja existente deve INCREMENTAR a quantidade, nao substituir.
    def test_adicionar_produto_existente_incrementa(self):
        e = Estoque()
        e.adicionar_produto("caneta", 10)
        e.adicionar_produto("caneta", 5)
        self.assertEqual(e.consultar_quantidade("caneta"), 15)

    # --- RED ---
    # Quantidade <= 0 nao e permitida.
    def test_adicionar_quantidade_zero_invalida(self):
        e = Estoque()
        with self.assertRaises(ValueError):
            e.adicionar_produto("caneta", 0)

    def test_adicionar_quantidade_negativa_invalida(self):
        e = Estoque()
        with self.assertRaises(ValueError):
            e.adicionar_produto("caneta", -3)


class TestConsultarQuantidade(unittest.TestCase):
    # --- RED ---
    # Consultar produto inexistente deve retornar 0.
    def test_consultar_inexistente_retorna_zero(self):
        e = Estoque()
        self.assertEqual(e.consultar_quantidade("borracha"), 0)


class TestRemoverProduto(unittest.TestCase):
    # --- RED ---
    def test_remover_produto_existente(self):
        e = Estoque()
        e.adicionar_produto("caneta", 10)
        e.remover_produto("caneta", 4)
        self.assertEqual(e.consultar_quantidade("caneta"), 6)

    def test_remover_quantidade_maior_que_disponivel(self):
        e = Estoque()
        e.adicionar_produto("caneta", 3)
        with self.assertRaises(ValueError):
            e.remover_produto("caneta", 5)

    def test_remover_produto_inexistente(self):
        e = Estoque()
        with self.assertRaises(ValueError):
            e.remover_produto("borracha", 1)

    def test_remover_quantidade_nao_positiva(self):
        e = Estoque()
        e.adicionar_produto("caneta", 5)
        with self.assertRaises(ValueError):
            e.remover_produto("caneta", 0)


class TestListarProdutos(unittest.TestCase):
    # --- RED ---
    def test_listar_apenas_com_quantidade_positiva(self):
        e = Estoque()
        e.adicionar_produto("caneta", 5)
        e.adicionar_produto("borracha", 2)
        e.remover_produto("borracha", 2)  # zera o estoque de borracha
        self.assertEqual(e.listar_produtos(), ["caneta"])

    def test_listar_estoque_vazio(self):
        e = Estoque()
        self.assertEqual(e.listar_produtos(), [])


class TestProdutoMaisEstocado(unittest.TestCase):
    # --- RED ---
    def test_produto_mais_estocado(self):
        e = Estoque()
        e.adicionar_produto("caneta", 5)
        e.adicionar_produto("lapis", 12)
        e.adicionar_produto("borracha", 3)
        self.assertEqual(e.produto_mais_estocado(), "lapis")

    def test_produto_mais_estocado_vazio_retorna_none(self):
        e = Estoque()
        self.assertIsNone(e.produto_mais_estocado())


if __name__ == "__main__":
    unittest.main()
