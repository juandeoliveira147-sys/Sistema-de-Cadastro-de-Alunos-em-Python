'''
cadastro de alunos
'''
import sys
import json
import time


def cadastrar_alunos():
    print("\n===Cadastro===")
    while True:
        nome_do_aluno = input("\nDigite o nome do aluno: ").strip().capitalize()
        teste = nome_do_aluno and all(c.isalpha() or c.isspace() for c in nome_do_aluno)
        if teste == True:
            break
        else:
            print("\nVerifique novamente se o nome está correto")
            continue
    while True:
        try:
            idade = int(input("\nDigite a idade do aluno: "))
        except ValueError:
            print("\nDigite apenas numeros para a idade do aluno!")
            continue
        if idade < 5 :
            print("\nA idade minima é 5, não será possivel realizar o cadastro!")
            return

        
        turma_do_aluno = input("\nDigite a turma do aluno: ").strip().capitalize()
        alunos = carregar_alunos()
        id_alunos = gerar_id(alunos)
        novo_aluno = {

            "nome" : nome_do_aluno,
            "idade" : idade,
            "turma" : turma_do_aluno,
            "id" : id_alunos
        }
        
        alunos.append(novo_aluno)
        salvar_alunos(alunos)
        print("\nNovo aluno cadastrado com sucesso!")
        time.sleep(2)
        return

    
def gerar_id(alunos):
    if alunos:
        return max(aluno["id"] for aluno in alunos) + 1
    return 1


def salvar_alunos(alunos):
    with open("alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(alunos , arquivo, indent=4 ,ensure_ascii=False)

def carregar_alunos():
    try:
        with open("alunos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

    
def ver_alunos():
    alunos = carregar_alunos()
    while True:
        if alunos:
            print("\n===Alunos===")
            for aluno in alunos:
                print(f"ID: {aluno["id"]}")
                print(f"Nome: {aluno["nome"]}")
                print(f"Idade: {aluno["idade"]}")
                print(f"Turma: {aluno["turma"]}")
                print("-" * 20)
            break
        else:
            print("\nSua lista de alunos está vazia!")
            time.sleep(2)
            return menu()
    while True:
        print("\n1 - Remover um aluno")
        print("\n2 - Voltar para o menu")
        escolha = input("\nEscolha: ").strip().lower()
        if escolha in ("2","menu"):
            print("\nVoltando...")
            return
        elif escolha in ("1","remover um aluno","remover"):
            deletar()
        else:
            print("\nOpção invalida!")
            continue
            
def deletar():
    
    alunos = carregar_alunos()
    if not alunos:
        print("\nNão tem alunos cadastrados!")
        time.sleep(2)
        menu()
    while True:
        try:
            id_aluno = int(input("Digite o ID do aluno: "))
        except ValueError:
            print("\nDigite os numeros do ID do aluno")
            continue
        break
    for aluno in alunos:

        if aluno["id"] == id_aluno:

            print("\nAluno encontrado!\n")
            print(f"ID: {aluno["id"]}")
            print(f"Nome: {aluno["nome"]}")
            print(f"Idade: {aluno["idade"]}")
            print(f"Turma: {aluno["turma"]}")
            print("-" * 20)

            while True:
                print("\n1- excluir o aluno")
                print("2- voltar para o menu\n")

                escolha = input("Escolha: ").strip().lower()

                if escolha in("1","excluir","excluir o aluno"):
                   #remover o aluno do arquivo json
                   alunos.remove(aluno)
                   salvar_alunos(alunos)
                   print("\nAluno excluido com sucesso!")
                   return

                elif escolha in("2","voltar para o menu","menu"):
                   return

                else:
                    print("\nVocê selecionou uma opção invalida")
                    continue
    print("\nAluno não encontrado")
    time.sleep(2)
    menu()


def alterar_aluno():

    alunos = carregar_alunos()
    if not alunos:
        print("\nNão tem alunos cadastrados!")
        time.sleep(2)
        menu()
    while True:
        try:
            id_aluno = int(input("Digite o ID do aluno: "))
        except ValueError:
            print("\nDigite os numeros do ID do aluno")
            continue
        break
    for aluno in alunos:

        if aluno["id"] == id_aluno:

            print("Aluno encontrado!")
            while True:
                nome = input("Novo nome: ").strip().capitalize()
                teste = nome and all(c.isalpha() or c.isspace() for c in nome)
                if teste == True:
                    break
                else:
                    print("\nVerifique novamente se o nome está correto")
                    continue
            while True:
                try:
                    idade = int(input("\nDigite a idade do aluno: "))
                except ValueError:
                    print("\nDigite apenas numeros para a idade do aluno!")
                    continue
                if idade < 5 :
                    print("\nA idade minima é 5 anos!")
                    continue
                else:
                    break
            turma = input("Nova turma: ").strip().capitalize()

            aluno["nome"] = nome
            aluno["idade"] = idade
            aluno["turma"] = turma
            salvar_alunos(alunos)

            print("Aluno alterado com sucesso!")
            menu()

    print("Aluno não encontrado!")
    time.sleep(2)
    return



def menu():
    print("\n=====Cadastro de alunos=====")
    while True:
        print("\n1 - Cadastrar aluno")
        print("\n2 - Ver alunos")
        print("\n3 - Alterar aluno")
        print("\n4 - Remover aluno")
        escolha = input("\n5 - Sair: ").strip().lower()


        if escolha in ("1","cadastrar aluno"):
            cadastrar_alunos()

        
        elif escolha in ("2","ver alunos"):
            ver_alunos()
        elif escolha in ("3","alterar aluno"):
            alterar_aluno()
        elif escolha in ("4","remover aluno","remover"):
            deletar()
        elif escolha in ("5","sair"):
            sys.exit()

        else:
            print("\nVocê selecionou uma opção invalida!")
            continue



if __name__ == "__main__":
    menu()