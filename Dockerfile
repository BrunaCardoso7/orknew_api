FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Criar diretórios necessários
RUN mkdir -p /app/staticfiles /app/media /app/nginx/ssl

# Configurar permissões dos certificados SSL (se existirem)
RUN if [ -f "/app/nginx/ssl/cloudflare.key" ]; then \
        chmod 600 /app/nginx/ssl/cloudflare.key; \
        echo "SSL key permissions set"; \
    fi

RUN if [ -f "/app/nginx/ssl/cloudflare.crt" ]; then \
        chmod 644 /app/nginx/ssl/cloudflare.crt; \
        echo "SSL certificate permissions set"; \
    fi

# Tornar o script executável
RUN chmod +x startup.sh

# Expor porta
EXPOSE 8000

# Executar script de inicialização
CMD ["./startup.sh"]