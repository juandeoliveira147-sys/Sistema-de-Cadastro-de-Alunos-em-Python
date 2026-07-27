#  Sistema de Cadastro de Alunos

Projeto desenvolvido em Python com o objetivo de praticar manipulação de arquivos JSON, listas, dicionários, funções e tratamento de exceções.

O sistema funciona como um pequeno banco de dados em arquivo JSON, permitindo cadastrar, consultar, alterar e excluir alunos através do terminal.

---

##  Funcionalidades

 Cadastro de alunos

 Listagem de todos os alunos

 Alteração de informações

 Exclusão de alunos

 Geração automática de IDs únicos

 Validação do nome

 Validação da idade

 Persistência de dados utilizando JSON

 Tratamento de erros de entrada

---

## 🛠️ Tecnologias utilizadas

- Python 3
- JSON
- Biblioteca json
- Biblioteca sys
- Biblioteca time

---


##  Estrutura do JSON

Cada aluno é armazenado como um dicionário dentro de uma lista.

Exemplo:

```json
[
    {
        "id": 1,
        "nome": "Felipe",
        "idade": 19,
        "turma": "Python"
    },
    {
        "id": 2,
        "nome": "Maria",
        "idade": 19,
        "turma": "Python"
    }
]
```

---

##  Funcionalidades implementadas

### Cadastro

Permite cadastrar novos alunos com:

- Nome
- Idade
- Turma

Cada aluno recebe automaticamente um ID único.

---

### Visualização

Lista todos os alunos cadastrados mostrando:

- ID
- Nome
- Idade
- Turma

---

### Alteração

Permite localizar um aluno através do ID e modificar suas informações.

---

### Exclusão

Permite remover um aluno utilizando seu ID.

Antes da exclusão, o sistema apresenta os dados do aluno para confirmação.

---

## ✔️ Validações

O sistema realiza diversas validações, como:

- Nome contendo apenas letras
- Idade numérica
- Idade mínima de 5 anos
- Tratamento de arquivo inexistente
- Tratamento de JSON inválido
- Verificação de lista vazia
- Tratamento de entradas incorretas

---

##  Conceitos praticados

Durante o desenvolvimento deste projeto foram utilizados conceitos como:

- Funções
- Listas
- Dicionários
- Estruturas de repetição
- Estruturas condicionais
- Manipulação de arquivos
- Arquivos JSON
- Tratamento de exceções
- Modularização
- CRUD
- Persistência de dados

---

##  Objetivo do projeto

Este projeto faz parte da minha jornada de estudos em Python e tem como objetivo consolidar conhecimentos fundamentais antes de avançar para bancos de dados relacionais, APIs e desenvolvimento web.

---

#### Sobre o projeto:

## Este projeto significa mais um passo no aprendizado da linguagem Python, irei me aprimorar e evoluir cada vez mais!
---
