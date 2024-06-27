FROM python:3.8-slim
WORKDIR /crud 
#copiar arquivos e instalar as dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# porta do Streamlit
EXPOSE 8501
# comando para rodar o projeto
CMD ["streamlit", "run", "main.py"]
