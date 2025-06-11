to deploy

SSH into server
cd into folder
/home/admin/om-django

kill any processes on 8000
sudo lsof -i :8000

git latest
git pull origin main

python manage.py collectstatic

start site
 gunicorn --bind 0.0.0.0:8000 odds-matcha.wsgi:application &
