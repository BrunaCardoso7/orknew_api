# Imagem base
FROM python:3.12-slim AS builder

RUN mkdir /app
WORKDIR /app

# Variável de ambiente para não gerar arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Atualiza e instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos
COPY requirements.txt /app/

# Instala as dependências Python
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# stage production
FROM python:3.12-slim

RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app


COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /app
COPY --chown=appuser:appuser . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER appuser

# Expõe a porta
EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

# Comando padrão
CMD ["/app/entrypoint.sh"]
