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


if __name__ == "__main__":
    unittest.main()
