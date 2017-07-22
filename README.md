python manage.py runserver 0.0.0.0:8000

source ~/.virtualenvs/djangodev/bin/activate
python manage.py runserver

virtualenv  myenv
. myenv/bin/activate

ssh-keygen -t rsa -C "example@gmail.com"
cat .ssh/id_rsa.pub
sudo apt-get install git
pip install -U channels

pip install -U redis
sudo apt-get install redis-server

sudo apt-get update
sudo apt-get install nginx
sudo apt-get install ufw
sudo ufw app list
sudo ufw allow 'Nginx HTTP'
sudo ufw status
sudo systemctl start nginx
- sudo systemctl stop nginx
- sudo systemctl restart nginx

cd /etc/nginx/sites-enabled/
sudo vim default

daphne firstproject.asgi:channel_layer

python manage.py runworker

server {

    listen 80;
    server_name example.org;
    charset utf-8;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}



CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
        "ROUTING": "firstproject.routing.channel_routing",
    },
}




