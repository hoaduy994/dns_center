IFS="/"
set -- $(pwd)
who=$3
ips=$(hostname -I | awk '{ print $1 }')
port=8800

# sudo apt update -y
# sudo apt upgrade -y
# sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y
# sudo apt autoremove -y
# wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
# tar -xf Python-3.9.1.tgz
# cd Python-3.9.1
# ./configure --enable-optimizations
# make -j 12
# sudo make altinstall
# sudo apt install python3-pip -y
# sudo apt update
# cd ..
# sudo rm -rf Python-3.9.1.tgz
# sudo rm -rf Python-3.9.1

sudo ufw allow 4444
sudo ufw allow 3000
sudo ufw allow 5555
sudo ufw allow 15672
# python3.9 -m venv venv
# venv/bin/pip install -r requirements.txt 
#install docker =.=
# /bin/sleep 10
# sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
# sudo apt-get update -y
# apt-cache policy docker-ce
# sudo apt install docker-ce -y
sudo systemctl enable --now docker
# sudo usermod -aG docker ${USER}
sudo usermod -aG docker ${who}


# install docker-compose =.=
/bin/sleep 10
# sudo apt-get install docker-compose -y

docker-compose --version
# run file docker
docker login -u fissecurity -p 74e9e79d-0d50-4a02-b84f-fa0ff7c02a98
sudo docker-compose up -d
#install rabbitmq
# /bin/sleep 10
# sudo apt-get install rabbitmq-server -y
# sudo apt-get update -y
# sudo apt-get upgrade -y
# sudo systemctl enable rabbitmq-server
# sudo rabbitmq-plugins enable rabbitmq_management
# sudo rabbitmqctl add_user admin password
# sudo rabbitmqctl set_user_tags admin administrator
# sudo rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"

mkdir service
mkdir nosql/nosql_json
sudo /home/hoadd4/dns_center/venv/bin/python manage.py migrate

/bin/sleep 10
# #runserver.service ###########################################
printf "[Unit]
Description=Send Log DNS To Server
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/hoadd4/dns_center
Environment=PYTHONPATH=/home/hoadd4/dns_center
ExecStartPre=/bin/sleep 30
ExecStart=/home/hoadd4/dns_center/venv/bin/python /home/hoadd4/dns_center/manage.py runserver $ips:$port
StandardInput=tty-force
Restart=on-failure
RestartSec=5s
StandardOutput=append:/home/hoadd4/dns_center/log/runserver_dns_center_output.log
StandardError=append:/home/hoadd4/dns_center/log/runserver_dns_center_error.log
[Install]
WantedBy=multi-user.target\n" > /home/hoadd4/dns_center/service/runserver_dns_center.service
sudo cp /home/hoadd4/dns_center/service/runserver_dns_center.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable runserver_dns_center.service
sudo systemctl start runserver_dns_center.service

##celery.service ###########################################

printf "[Unit]
Description=Send Log DNS To Server
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/hoadd4/dns_center
Environment=PYTHONPATH=/home/hoadd4/dns_center
ExecStartPre=/bin/sleep 40
ExecStart=/home/hoadd4/dns_center/venv/bin/celery -A DNS_Center --loglevel=info worker
StandardInput=tty-force
Restart=on-failure
RestartSec=5s
StandardOutput=append:/home/hoadd4/dns_center/log/celery_dns_center_output.log
StandardError=append:/home/hoadd4/dns_center/log/celery_dns_center_error.log

[Install]
WantedBy=multi-user.target\n" > /home/hoadd4/dns_center/service/celery_dns_center.service
sudo cp /home/hoadd4/dns_center/service/celery_dns_center.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable celery_dns_center.service
sudo systemctl start celery_dns_center.service