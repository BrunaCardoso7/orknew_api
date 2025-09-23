FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements primeiro para aproveitar o cache do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Criar diretórios necessários e configurar SSL
RUN mkdir -p /app/staticfiles /app/media && \
    if [ -f "nginx/ssl/cloudflare.key" ]; then chmod 600 nginx/ssl/cloudflare.key; fi && \
    if [ -f "nginx/ssl/cloudflare.crt" ]; then chmod 644 nginx/ssl/cloudflare.crt; fi

# Tornar o entrypoint executável
RUN chmod +x entrypoint.sh

# Expor porta
EXPOSE 8000

# Usar o entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]