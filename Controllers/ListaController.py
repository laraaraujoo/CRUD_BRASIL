import serv.database as banco

def Criar(criar):
    count = banco.cursor.execute ("""
    INSERT INTO Tarefas (tarefa,Descricao)
    VALUES (?,?)""",
    criar.tarefa, criar.descricao).rowcount
    banco.conn.commit()

                            