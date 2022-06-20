# sSnakeFramework  (nome temporario kkk)


## Ideia Base
Ser uma aplicação de base para desenvolvimento web em Python.

<br><br>

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
py snake make controller [name]
```
Criar um model
```
py snake make model [name]
```
Criar uma migração
```
py snake make migration [name]
```
Criar um seeder
```
py snake make seeder [name]
```
Listar rotas
```
py snake list routes
```
Iniciar o server
```
py snake server
```
Migrar banco de dados
```
py snake migrate [fresh]
```
Ajuda geral
```
py snake help
```


