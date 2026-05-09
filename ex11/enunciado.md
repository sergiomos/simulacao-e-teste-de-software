## Objetivo
Configurar um pipeline de CI com GitHub Actions para um repositório Python já
existente, fazendo-o passar por todas as etapas: lint, testes e cobertura
mínima.

## Repositório base:
Acesse: github.com/rossi-luciano/
teste_de_software
Faça um fork para sua conta pessoal do
GitHub
Clone o fork localmente e crie uma
branch: git checkout -b pipeline

## O repositório contém:
calculadora.py - 6 funções
test_calculadora.py - testes
incompletos (cobertura ≈ 65%)
requirements.txt
README.md com instruções

## Entregas (3 etapas)
Etapa 1: criar o arquivo
.github/workflows/ci.yml
com lint + testes + cobertura
(-cov-fail-under=80)
Etapa 2: observar o pipeline
falhar por cobertura insuficiente -
identificar as funções não cobertas
Etapa 3: escrever os testes que
faltam e fazer o pipeline passar

## O pipeline deve conter
1 Trigger: push e pull_request para
main
2 Setup Python 3.11
3 Instalação via requirements.txt
4 Step de lint (flake8)
5 Step de testes com cobertura mínima de
80%
6 Publicação do relatório como artefato

## Entrega
Link para o repositório (fork) com:
Arquivo ci.yml presente
Badge de status passing no
README.md
Histórico de commits mostrando a
progressão: pipeline vermelho
→ testes adicionados →
pipeline verde
Atenção
O histórico de commits faz parte da
avaliação - não entregue apenas o
estado final.