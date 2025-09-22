#!/usr/bin/env bash

echo "🚀 Iniciando aplicação Django..."

# Definir permissões corretas para os certificados SSL
echo "🔐 Configurando permissões dos certificados SSL..."
if [ -f "/app/nginx/ssl/cloudflare.key" ]; then
    chmod 600 /app/nginx/ssl/cloudflare.key
    echo "✅ Permissões do cloudflare.key configuradas (600)"
else
    echo "⚠️  Arquivo cloudflare.key não encontrado em /app/nginx/ssl/"
fi

if [ -f "/app/nginx/ssl/cloudflare.crt" ]; then
    chmod 644 /app/nginx/ssl/cloudflare.crt
    echo "✅ Permissões do cloudflare.crt configuradas (644)"
else
    echo "⚠️  Arquivo cloudflare.crt não encontrado em /app/nginx/ssl/"
fi

# Instalar dependências
echo "📦 Instalando dependências..."
pip install -r requirements.txt

# Executar migrações
echo "🗃️  Executando migrações do banco de dados..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Coletar arquivos estáticos
echo "📁 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

# Criar superusuário se não existir (opcional)
echo "👤 Verificando superusuário..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@orknew.dev')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"✅ Superusuário '{username}' criado com sucesso!")
else:
    print("ℹ️  Superusuário já existe ou DJANGO_SUPERUSER_PASSWORD não definida")
EOF

# Verificar se o banco está conectado
echo "🔍 Testando conexão com o banco de dados..."
python manage.py check --database default

# Iniciar o servidor Gunicorn
echo "🌐 Iniciando servidor Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 core.wsgi:application