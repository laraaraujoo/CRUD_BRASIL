class Lista:
    def __init__(self,tarefa,descricao):
        self.tarefa = tarefa
        self.descricao = descricao
        

minha_lista = Lista(tarefa='estudar', descricao='teste')

print(minha_lista.tarefa) 
print(minha_lista.descricao)  