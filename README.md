# Sistema de Competições (POO + PyQt5 + MySQL)

Projeto acadêmico com organização em camadas (model / view / controller), interface PyQt5 e persistência em MySQL.

## Requisitos
- Python 3.10+
- MySQL Server funcionando localmente
- Biblioteca: `PyQt5`, `mysql-connector-python`

## Instalação
```bash
# (opcional) criar venv
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
```

## Banco de Dados
Crie o schema e tabelas executando o script:
```sql
-- no cliente do MySQL
SOURCE caminho/para/sql/schema.sql;
```
Ou copie e cole o conteúdo manualmente.

## Configuração da conexão
Edite `model/database.py` e ajuste `host`, `user`, `password` e `database`.

## Executar
```bash
python main.py
```

## Funcionalidades
- Cadastrar **equipes** e **membros** (CRUD)
- Cadastrar **provas** (teórica / prática) com **polimorfismo** no cálculo da pontuação
- Visualizar resultados (listagens)
- Tratamento de erros com `try/except` e mensagens para o usuário

## Estrutura
```
projeto_poo_competicoes/
  controller/
  model/
  view/
  sql/schema.sql
  main.py
```
