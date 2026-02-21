## Classes de Equivalência

| Classe | Descrição                                      |   Tipo   |
| :----- | :--------------------------------------------- | :------: |
| CE1    | Peso zero ou negativo                          | Inválido |
| CE2    | Peso não é número                              | Inválido |
| CE3    | Destino não é string                           | Inválido |
| CE4    | Valor do pedido não é número                   | Inválido |
| CE5    | Valor do pedido zero ou negativo               | Inválido |
| CE6    | Peso acima de 20kg                             | Inválido |
| CE7    | Sem destino                                    | Inválido |
| CE9    | Peso entre 0 e 20 (exclusivo) e tipos corretos |  Válido  |

## Valores Limites


| Valor | Classe |     Status      |
| :---- | :----- | :-------------: |
| -0.1  | CE1    |    Inválido     |
| 0     | CE1    |    Inválido     |
| 20    | CE2    |    Inválido     |
| 20.1  | CE2    |    Inválido     |
| 0.1   | CE3    | Válido (mínimo) |
| 19.9  | CE3    | Válido (maximo) |

## Tabela de Decisão
| Condição                      | R1       | R2       | R3       | R4       | R5       | R6       | R7       | R8       | R9          | R10     |
| :---------------------------- | :------- | :------- | :------- | :------- | :------- | :------- | :------- | :------- | :---------- | :------ |
| Peso entre 0 e 20 (exclusivo) | S        | S        | S        | S        | S        | S        | S        | S        | S           |         |
| Peso até 1Kg                  | S        | S        | S        | N        | N        | N        | N        | N        | N           | -       |
| Peso de 1.1kg a 5Kg           | N        | N        | N        | S        | S        | S        | N        | N        | N           | -       |
| Peso de 5.1 a 20 kg           | N        | N        | N        | N        | N        | N        | S        | S        | S           | -       |
| Peso acima de 20 Kg           | N        | N        | N        | N        | N        | N        | N        | N        | N           | -       |
| Valor do Pedido > 200         | N        | N        | N        | N        | N        | N        | N        | N        | N           | -       |
| Mesma região                  | S        | N        | N        | S        | N        | N        | N        | S        | N           | -       |
| Outra região                  | N        | S        | N        | N        | S        | N        | N        | N        | S           | -       |
| Internacional                 | N        | N        | S        | N        | N        | S        | S        | N        | N           | -       |
| **Resultado**                 |          |          |          |          |          |          |          |          |             |         |
| Valor do Frete                | R$ 10,00 | R$ 15,00 | R$ 20,00 | R$ 15,00 | R$ 22,50 | R$ 30,00 | R$ 50,00 | R$ 25,00 | R$ 37,50,00 | R$ 0,00 |

