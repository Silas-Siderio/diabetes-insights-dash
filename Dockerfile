# Usar imagem base oficial do Python
FROM python:3.10-slim

# Diretório de trabalho no container
WORKDIR /app

# Copiar arquivos do projeto
COPY . /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor porta padrão do Dash
EXPOSE 7860

# Comando de inicialização
CMD ["python", "app.py"]
