import json


caminho_json = "campeoes-lol.json"


with open(caminho_json, "r", encoding="utf-8") as arquivo:
    campeoes = json.load(arquivo)


def salvar():
    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(campeoes, arquivo, ensure_ascii=False, indent=4)


def ler_id():
    while True:
        try:
            return int(input("digite o ID do campeão: "))
        except ValueError:
            print("ID inválido. Digite um número inteiro.")


def mostrar(lista):
    if len(lista) == 0:
        print("Nenhum campeão encontrado.")
    else:
        for campeao in lista:
            print(
                campeao["id"], "-",
                campeao["nome"], "-",
                campeao["funcao"], "-",
                campeao["classe"], "-",
                campeao["dificuldade"]
            )


def incluir():
    novo_id = 1

    if len(campeoes) > 0:
        novo_id = campeoes[-1]["id"] + 1

    nome = input("nome: ")
    funcao = input("função: ")
    classe = input("classe: ")
    dificuldade = input("dificuldade (facil, media ou dificil): ")

    campeoes.append({
        "id": novo_id,
        "nome": nome,
        "funcao": funcao,
        "classe": classe,
        "dificuldade": dificuldade
    })

    salvar()
    print("campeão incluído com sucesso.")


def alterar():
    id_alvo = ler_id()
    encontrado = False

    for campeao in campeoes:
        if campeao["id"] == id_alvo:
            encontrado = True
            campeao["nome"] = input("novo nome: ")
            campeao["funcao"] = input("nova função: ")
            campeao["classe"] = input("nova classe: ")
            campeao["dificuldade"] = input("nova dificuldade: ")
            salvar()
            print("campeão alterado com sucesso.")
            break

    if not encontrado:
        print("campeão não encontrado.")


def excluir():
    id_alvo = ler_id()
    encontrado = False

    for campeao in campeoes:
        if campeao["id"] == id_alvo:
            campeoes.remove(campeao)
            encontrado = True
            salvar()
            print("campeão excluído com sucesso.")
            break

    if not encontrado:
        print("campeão não encontrado.")


def pesquisar():
    texto = input("digite parte do nome ou da função: ").lower()
    resultado = []

    for campeao in campeoes:
        nome = campeao["nome"].lower()
        funcao = campeao["funcao"].lower()

        if texto in nome or texto in funcao:
            resultado.append(campeao)

    mostrar(resultado)


def chave_nome(campeao):
    return campeao["nome"].lower()


def chave_funcao(campeao):
    return campeao["funcao"].lower()


def listar_por_nome():
    lista = sorted(campeoes, key=chave_nome)
    mostrar(lista)


def listar_por_funcao():
    lista = sorted(campeoes, key=chave_funcao)
    mostrar(lista)


print("\n=== Cadastro de Campeões ===")
print("1 - Incluir campeão")
print("2 - Alterar campeão")
print("3 - Excluir campeão")
print("4 - Pesquisar por nome ou função")
print("5 - Listar por nome")
print("6 - Listar por função")

opcao = input("escolha uma opção: ")

if opcao == "1":
    incluir()
else:
    if opcao == "2":
        alterar()
    else:
        if opcao == "3":
            excluir()
        else:
            if opcao == "4":
                pesquisar()
            else:
                if opcao == "5":
                    listar_por_nome()
                else:
                    if opcao == "6":
                        listar_por_funcao()