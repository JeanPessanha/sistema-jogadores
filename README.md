# Sistema de Jogadores

Projeto final do **Mundo 2** do curso de Python do Gustavo Guanabara (Curso em Vídeo).
É um sistema de cadastro de jogadores feito para o terminal, usando apenas os conceitos vistos até o Mundo 2.

## Funcionalidades

- **Cadastrar jogador:** nome, idade e time (com validação para aceitar só números na idade)
- **Listar jogadores:** mostra uma tabela com todos os jogadores cadastrados
- **Pesquisar jogador:** informa se um nome (ou parte dele) está cadastrado
- **Ver estatísticas:** total de jogadores, idade média, jogador mais velho e mais novo
- **Sair:** encerra o programa

## Conceitos aplicados

- Laços `while` e `for`
- Condicionais `if / elif / else`
- Contadores e acumuladores
- Manipulação de strings (`strip`, `title`, `lower`, `isnumeric`)
- Formatação com f-strings
- Módulo `time` (`sleep`) para a animação de "cadastrando..."

## Como executar

É necessário ter o Python 3 instalado. No terminal, dentro da pasta do projeto:

```bash
sistema_jogadores.py
```

## Limitações conhecidas

- Os dados não são salvos: ao fechar o programa, os jogadores cadastrados são perdidos.
- A pesquisa só informa se o jogador existe, sem mostrar os dados dele, porque ainda não foram vistas listas e dicionários.
- As Opções 2 e 4 não estão funcionando por enquanto

## Próximos passos

Refazer o projeto no Mundo 3 usando listas, dicionários e funções, e depois adicionar persistência dos dados em arquivo.

## Autor

Jean Pessanha — [github.com/JeanPessanha](https://github.com/JeanPessanha)
