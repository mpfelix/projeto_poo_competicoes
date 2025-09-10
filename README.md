# Projeto POO - Sistema de Competições

Trabalho desenvolvido para a disciplina de **Programação Orientada a Objetos (POO)**.  
O objetivo é criar um sistema em **Python + PyQt5** para gerenciar **equipes, provas e resultados** em competições acadêmicas, aplicando conceitos de **classes, herança, polimorfismo e encapsulamento**.

---

##  Componente
- Maria Paula Felix

---

## Funcionalidades
O sistema permite:
-  **Cadastrar equipes** e adicionar/remover membros manualmente  
-  **Cadastrar provas** teóricas e práticas  
  - Prova Teórica → número de questões  
  - Prova Prática → tempo limite  
-  **Calcular pontuação** automaticamente (usando **polimorfismo**)  
-  **Visualizar resultados** em tela gráfica  
-  **Tratar erros** com `try/except` e mensagens para o usuário  
-  **Armazenar dados** em listas ou banco MySQL (opcional)  

---

##  Estrutura do Projeto

projeto_poo_competicoes/
│── main.py # Arquivo principal da aplicação
│── requirements.txt # Dependências do projeto
│── README.md # Documentação
│
├── controller/ # Controladores (ligam model ↔ view)
│ ├── controller_equipes.py
│ ├── controller_provas.py
│ ├── controller_resultados.py
│
├── model/ # Regras de negócio e dados
│ ├── equipe.py
│ ├── prova.py
│ ├── resultado.py
│ ├── database.py (opcional p/ MySQL)
│
└── view/ # Telas gráficas (QtDesigner)
├── tela_principal.ui / .py
├── cadastro_equipes.ui / .py
├── cadastro_provas.ui / .py
├── cadastro_membros.ui / .py
├── visualizar_resultados.ui / .py
