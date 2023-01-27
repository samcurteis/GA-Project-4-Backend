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

echo "inserting authors"
python manage.py loaddata authors/seeds.json

echo "inserting comments"
python manage.py loaddata comments/seeds.json

echo "inserting posts"
python manage.py loaddata posts/seeds.json

