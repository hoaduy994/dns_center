

# Server Dns Node

## Development

> **Note:**
 >- Ubuntu server 20.04
 >- Python 3.9
 >- [Docker](https://docs.docker.com/engine/install/ubuntu/)
 >- [Docker Compose](https://docs.docker.com/compose/install/)

**Virtualenv**
```  
python3.9 -m venv venv
```

```  
source ./venv/scripts/activate
```
**Install dependencies**
```  
(venv) inhdi@dnscenter:~/dns_center$ pip install -r requirements.txt
```
**Run docker compose**
```  
(venv) inhdi@dnscenter:~/dns_center$ sudo docker-compose up
```
**Run Server**
```  
(venv) inhdi@dnscenter:~/dns_center$ python manage.py migrate
```
```  
(venv) inhdi@dnscenter:~/dns_center$ python manage.py runserver
```
```  
(venv) inhdi@dnscenter:~/dns_center$ python manage.py createsuperuser
```

## Open Server
**App API**
```  
 http://127.0.0.1:8000/api/swagger/
```
![enter image description here](https://i.imgur.com/kwm62zV.png)
----------
**pgAdmin**
```  
 http://127.0.0.1:4444
```
![enter image description here](https://i.imgur.com/s9ntNka.png)
```  
EMAIL: admin@dnscenter.com
PASSWORD: csc@123A
```
----------
**Postgres**
```  
USER: admin
PASSWORD: csc@123A
Port: 5555
```

## Server Dev PRO

**App API**
```  
http://10.15.152.224:8800/api/swagger/
```
```  
EMAIL: dangnh51
PASSWORD: csc@123a
```
----------
**pgAdmin**
```  
http://10.15.152.224:4444/
```
```  
EMAIL: admin@dnscenter.com
PASSWORD: csc@123A
```
