echo "dropping database poems"
dropdb poems

echo "creating database poems"
createdb poems

python manage.py makemigrations

python manage.py migrate

echo "inserting users"
python manage.py loaddata jwt_auth/seeds.json

echo "inserting poems"
python manage.py loaddata poems/seeds.json