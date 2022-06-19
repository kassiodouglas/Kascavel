# SnakeFramework


## Ideia Base
Ser uma aplicação de base para desenvolvimento web em Python.

<br><br>

## Objetivo Base
SnakeFramework é um framework de aplicação web com sintaxe facil, organizada e elegante. Liberamos acesso para criar o que quiser em uma estrutura totalmente organizada.

<br><br>

## Porque usar o SnakeFramework?

O SnakeFramework entende que valorizar a organização e os detalhes dos códigos, evita simultâneas interações de todos os lados propensas a erros. Sobre esta problemática estruturamos todo o SnakeFramework. A sintaxe e simples e elegante e funcional tudo isso disponivel para seus melhores projetos. Os recursos ainda estão em desenvolvimento mas temos a missão de criar uma experiência maravilhosa para sua aplicação e seu desemvolvimento Back-End e Front-End.


## Como Instalar
____
Rode no terminal do vs code os comandos abaixo:

Criar ambiente virtual:
```
python -m venv NOME_DO_AMBIENTE
```

Ativar ambiente:
```
.\NOME_DO_AMBIENTE\Scripts\activate.bat
```

Instalar pacotes:
```
pip install -r requirements.txt
```


<br><br>

## A cada novo pacote instalado:
____
Para atualizar o arquivo requirements.txt 
```
pip freeze > requirements.txt 
```


<br><br>

## Comandos:
____
Criar um controlador
```
py main.py make controller [name]
```
Criar um model
```
py main.py make model [name]
```
Criar uma migração
```
py main.py make migration [name]
```
Criar um seeder
```
py main.py make seeder [name]
```
Listar rotas
```
py main.py list routes
```
Iniciar o server
```
py main.py server
```
Migrar banco de dados
```
py main.py migrate [fresh]
```
Ajuda geral
```
py main.py help
```


