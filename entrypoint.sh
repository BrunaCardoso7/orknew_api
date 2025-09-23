#!/usr/bin/env bash

echo "🚀 Iniciando aplicação Django..."

# Instalar dependências
echo "📦 Instalando dependências..."
pip install -r requirements.txt

# Executar migrações
echo "🗃️ Executando migrações do banco de dados..."
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
    print("ℹ️ Superusuário já existe ou senha não definida")
EOF

# Verificar conexão com banco
echo "🔍 Testando conexão com banco de dados..."
python manage.py check --database default

# Iniciar servidor
echo "🌐 Iniciando servidor Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 --timeout 120 core.wsgi:application