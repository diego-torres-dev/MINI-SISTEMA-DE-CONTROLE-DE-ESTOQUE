# Estoque mínimo por categoria
estoque_min_alimentos = 50
estoque_min_bebidas = 75
estoque_min_limpeza = 30

# Obtenção de dados com o usuário
produto = input("Digite o nome do produto:\n")
categoria = input("Digite a categoria do produto:\n")
qtde_estoque = input("Informe a quantidade em estoque:\n")

# Verifica se todos os campos foram preenchidos
if produto and categoria and qtde_estoque:
    # Converte o texto em número inteiro
    qtde_estoque = int(qtde_estoque)

    if categoria.casefold() == "alimentos":
        if qtde_estoque < estoque_min_alimentos:
            print(f"Solicitar {produto} à equipe de compras. Temos apenas {qtde_estoque} unidades em estoque.")
        else:
            pass
    elif categoria.casefold() == "bebidas":
        if qtde_estoque < estoque_min_bebidas:
            print(f"Solicitar {produto} à equipe de compras. Temos apenas {qtde_estoque} unidades em estoque.")
        else:
            pass
    elif categoria.casefold() == "limpeza":
        if qtde_estoque < estoque_min_limpeza:
            print(f"Solicitar {produto} à equipe de compras. Temos apenas {qtde_estoque} unidades em estoque.")
        else:
            pass
    else:
        print("A categoria informada não existe.")
else:
    print("Por favor, preencha todos os campos.")
    