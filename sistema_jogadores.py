from time import sleep

TOTAL = 0
SOMA_IDADES = 0
NOME_MAIS_VELHO = ""
MAIOR_IDADE = 0
NOME_MAIS_NOVO = ""
MENOR_IDADE = 0
LISTA = ""
NOMES = ""
while True:
    print("="*30)
    print("Sistema de Jogadores".center(30))
    print("="*30)
    print("")
    print("[1] Cadastrar jogador")
    print("[2] Listar jogador ")
    print("[3] Pesquisar jogador")
    print("[4] Ver estatisticas jogador")
    print("[5] Sair")
    OPCAO = input("Digite a opção desejada: ").strip()
    print("")
    if OPCAO == "1" :
        NOME = str(input("Digite o nome do Jogador: ")).strip().title()
        IDADE= (input("Digite a idade do Jogador: ")).strip()
        while not IDADE.isnumeric():
           print("ERROR Digite apenas numeros!")
           IDADE = input("idade do Jogador: ").strip()
        IDADE = int(IDADE)
        TIME = str(input("TIME do jogador: ")).strip().title()
        print("cadastrando", end="", flush=True)
        for _ in range(3):
            sleep(0.3)
            print(".", end="", flush=True)    
        print("pronto")
        TOTAL += 1
        SOMA_IDADES += IDADE

        if TOTAL == 1: 
            MAIOR_IDADE = MENOR_IDADE = IDADE
            NOME_MAIS_VELHO = NOME_MAIS_NOVO = NOME
        else:
            if IDADE > MAIOR_IDADE:
                MAIOR_IDADE = IDADE
                NOME_MAIS_VELHO = NOME
            if IDADE < MENOR_IDADE:
                MENOR_IDADE = IDADE
                NOME_MAIS_NOVO = NOME
        LISTA += f"{NOME:<20}{IDADE:<7}{TIME}\n"
        NOMES += NOME.lower() + " | "

    elif OPCAO == "2":
        if TOTAL == 0:
            print("Nenhum jogador cadastrado.")
        else:
            print(f"{NOME:<20}{IDADE:<7}{TIME}")
            print("-" * 40)
            print(LISTA, end="")           
           
    elif OPCAO == "3":
           BUSCA = input("Nome (ou parte do nome): ").strip().lower()
           if BUSCA in NOMES:
               print("Jogador encontrado!")
               print(NOMES)
           else:
               print("Jogador não encontrado.")
   
    elif OPCAO == "4":
           if TOTAL == 0:
               print("Nenhum jogador cadastrado.")
           else:
               print(f"Total de jogadores: {TOTAL}")
               print(f"Idade média: {SOMA_IDADES / TOTAL:.1f} anos")
               print(f"Mais velho: {NOME_MAIS_VELHO} ({MAIOR_IDADE} anos)")
               print(f"Mais novo: {NOME_MAIS_NOVO} ({MENOR_IDADE} anos)")
   
    elif OPCAO == "5":
           print("Encerrando programa. Até logo!")
           break
   
    else:
      print("Opção inválida! Escolha de 1 a 5.")
   
    print()
    
