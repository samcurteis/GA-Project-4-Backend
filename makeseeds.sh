echo "creating poems/seeds.json"
python manage.py dumpdata poems --output poems/seeds.json --indent=2;

echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;