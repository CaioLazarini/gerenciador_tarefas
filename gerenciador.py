class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "✓" if self.concluida else "✗"
        return f"{status} {self.descricao}"

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        nova_tarefa = Tarefa(descricao)
        self.tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
        for index, tarefa in enumerate(self.tarefas):
            print(f"{index + 1}. {tarefa}")

    def concluir_tarefa(self, index):
        if 0 <= index < len(self.tarefas):
            self.tarefas[index].concluir()
            print(f"Tarefa '{self.tarefas[index].descricao}' marcada como concluída.")
        else:
            print("Índice de tarefa inválido.")

    def executar(self):
        while True:
            print("\nGerenciador de Tarefas")
            print("1. Adicionar Tarefa")
            print("2. Listar Tarefas")
            print("3. Concluir Tarefa")
            print("4. Sair")
            
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                descricao = input("Descrição da tarefa: ")
                self.adicionar_tarefa(descricao)
                print("Tarefa adicionada.")

            elif escolha == "2":
                self.listar_tarefas()

            elif escolha == "3":
                index = int(input("Número da tarefa a ser concluída: ")) - 1
                self.concluir_tarefa(index)

            elif escolha == "4":
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")