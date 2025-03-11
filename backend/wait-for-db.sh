
echo "Aguardando o MySQL iniciar..." 

until mysql -h db -u user1 -p123 restaurant; do
  echo "Aguardando conexão com o banco de dados..."
  sleep 2
done

echo "Banco de dados disponível!"

echo "Executando migrações..."
alembic upgrade head

echo "Populando banco de dados..."
python -m app.populate_db

echo "Iniciando backend..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
