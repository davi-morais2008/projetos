# Lista de Tarefas em Python 📝

Programa simples para gerenciar uma lista de tarefas pelo terminal, permitindo adicionar, remover, listar e concluir tarefas.  
As tarefas são salvas automaticamente em um arquivo `.txt`, garantindo que os dados permaneçam entre execuções do programa.

---

## 🚀 Funcionalidades

- ➕ **Adicionar tarefa**  
- 🗑 **Remover tarefa**  
- 📋 **Listar tarefas** com indicação de status ([ ] pendente, [x] concluída)  
- ✔ **Concluir tarefa**  
- 💾 **Persistência automática** das tarefas em arquivo `.txt`

---

## 📁 Estrutura do projeto

```
.
├── funcoes.py           # Funções para manipulação da lista e do arquivo
├── main.py              # Programa principal que roda o menu interativo
├── tarefas.txt          # Arquivo gerado automaticamente para salvar as tarefas
└── README.md            # Documentação do projeto
```

---

## 🛠 Tecnologias utilizadas

- Python 3.x  
- Manipulação de arquivos `.txt`  
- Estruturas de dados (listas)

---

## 💻 Como usar

1. Execute o programa:  
   ```bash
   python main.py
   ```

3. Use o menu interativo para gerenciar suas tarefas.

---

## 📌 Observações

- O arquivo `tarefas.txt` será criado automaticamente na primeira execução, se não existir.  
- As tarefas concluídas são marcadas com `[x]` no arquivo e na listagem do terminal.  
- Ao remover ou concluir uma tarefa, o arquivo é atualizado automaticamente.

---

## 👨‍💻 Autor

Desenvolvido por **Davi Morais**.

---
