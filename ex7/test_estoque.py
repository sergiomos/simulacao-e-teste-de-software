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


if __name__ == "__main__":
    unittest.main()
