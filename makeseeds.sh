echo "creating poems/seeds.json"
python manage.py dumpdata poems --output poems/seeds.json --indent=2;

echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;

echo "creating authors/seeds.json"
python manage.py dumpdata authors --output authors/seeds.json --indent=2;

echo "creating comments/seeds.json"
python manage.py dumpdata comments --output comments/seeds.json --indent=2;

echo "creating poems/seeds.json"
python manage.py dumpdata poems --output poems/seeds.json --indent=2;

echo "creating posts/seeds.json"
python manage.py dumpdata posts --output posts/seeds.json --indent=2;