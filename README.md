Visit “104.197.99.74:8000/snake" to play Snake

![Alt text](/snake.png?raw=true "Cover")

----------------------------------------------

# Developer Notes

Google Cloud Terminal
$ sudo apt-get install python3-pip  
$ pip3 install virtualenv  
$ virtualenv --python=`which python3` ~/.virtualenvs/djangodev  
$pip install -U channels  
$pip install -U redis  
$sudo apt-get install redis-server  


# Activate Django:  
. myenv/bin/activate  
Otherwise:  
source ~/.virtualenvs/djangodev/bin/activate  


# Start Server:   
Linux Screen - ctrl-a-c  
python manage.py runserver 0.0.0.0:8000  

If port is taken:  
ps aux | grep -i manage  
kill -9 pid (second number from left)  

Nginx and Daphne:  
sudo apt-get update  
sudo apt-get install nginx  
sudo apt-get install ufw  
sudo ufw app list  
sudo ufw allow 'Nginx HTTP'  
sudo ufw status  
sudo systemctl start nginx  
sudo systemctl stop nginx  
sudo systemctl restart nginx   

cd /etc/nginx/sites-enabled/  
sudo vim default  
daphne firstproject.asgi:channel_layer  
python manage.py runworker  

```
server {
    listen 80;
    server_name example.org;
    charset utf-8;
    #listen 443 ssl;
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
 
$ daphne firstproject.asgi:channel_layer
