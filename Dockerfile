# syntax=docker/dockerfile:1

FROM python:3.12-slim
WORKDIR /app

# Copia apenas requirements e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY src/ src/
COPY tests/ tests/

# Define variável de ambiente para testes
ENV PYTHONPATH=/app

# Comando padrão (pode ser sobrescrito pelo container)
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]
