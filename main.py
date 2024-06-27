import json
from bson import ObjectId
import streamlit as st;
import model.Lista as Lista;
from pymongo import MongoClient, errors


try:
    #testar cnx local
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000) # teste de 5s para se conectar com o servidor 
    db = client['CRUDDB'] #banco e o nome ta tabela
    items_collection = db['tarefas']
    client.server_info()
    st.success("Conectado ao MongoDB com sucesso!")
except errors.ServerSelectionTimeoutError as err:
    st.error(f"Erro de conexão com o MongoDB: {err}")
    st.stop()


# para mostrar todas as tarefas
def get_tarefas():
    tarefas = list(items_collection.find())
    for tarefa in tarefas:
        tarefa['_id'] = str(tarefa['_id'])
    return tarefas

# para add uma nova tarefa 
def add_tarefa(titulo, descricao):
    tarefa = {"titulo": titulo, "descricao": descricao}
    tarefa_id = items_collection.insert_one(tarefa).inserted_id
    new_tarefa = items_collection.find_one({"_id": ObjectId(tarefa_id)})
    new_tarefa['_id'] = str(new_tarefa['_id'])

    return new_tarefa

# tarefas com ID
def get_tarefa(id):
    tarefa = items_collection.find_one({"_id": ObjectId(id)})
    if tarefa:
        tarefa['_id'] = str(tarefa['_id'])
        return tarefa
    else:
        return None

# atualizar tarefa
def update_tarefa(id, titulo, descricao):
    data = {"titulo": titulo, "descricao": descricao}
    result = items_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count:
        updated_tarefa = items_collection.find_one({"_id": ObjectId(id)})
        updated_tarefa['_id'] = str(updated_tarefa['_id'])
        return updated_tarefa
    else:
        return None

# deleta tarefa
def delete_tarefa(id):
    result = items_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return True
    else:
        return False


# criando a interface com o streamlit
st.title("To Do List")

with st.form(key="crud"):
    input_tarefa = st.text_input(label="Título da tarefa")
    input_descricao = st.text_input(label="Descrição da tarefa")
    input_btcriar = st.form_submit_button("Criar")
    input_btdelete = st.form_submit_button("Deletar")
    input_btatualizar = st.form_submit_button("Atualizar")
    input_btlistar = st.form_submit_button("Listar")

# função do botao criar
if input_btcriar:
    nova_tarefa = add_tarefa(input_tarefa, input_descricao) 
    st.write(f"Tarefa criada: {nova_tarefa}")


if input_btlistar:
    tarefas = get_tarefas() 
    if tarefas:
        st.write("Lista de Tarefas:")
        for tarefa in tarefas:
            st.write(f"ID: {tarefa['_id']}, Título: {tarefa['titulo']}, Descrição: {tarefa['descricao']}")
    else:
        st.write("Não há tarefas cadastradas.")


# botão para atualizar tarefa
if input_btatualizar:
    id_tarefa = input_btatualizar.strip()  # remover espaços em branco
    if id_tarefa:
        tarefa = get_tarefa(id_tarefa)
        if tarefa:
            updated_tarefa = update_tarefa(id_tarefa, input_tarefa, input_descricao)
            st.write(f"Tarefa atualizada com sucesso: {updated_tarefa}")
        else:
            st.write(f"Nenhuma tarefa encontrada com o ID: {id_tarefa}")
    else:
        st.write("Por favor, insira um ID válido para atualizar a tarefa.")