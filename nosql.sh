IFS="/"
set -- $(pwd)
who=$3
cd nosql

##dashboard_dns_center.service ###########################################

printf "[Unit]
Description=Save file json dashboard
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/dangnh51/dns_center
Environment=PYTHONPATH=/home/dangnh51/dns_center
ExecStartPre=/bin/sleep 5
ExecStart=/home/dangnh51/dns_center/venv/bin/python /home/dangnh51/dns_center/nosql/dashboard.py
StandardInput=tty-force
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target\n" > /home/dangnh51/dns_center/service/dashboard_dns_center.service
sudo cp /home/dangnh51/dns_center/service/dashboard_dns_center.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable dashboard_dns_center.service
sudo systemctl start dashboard_dns_center.service


##datadnsnode_dns_center.service ###########################################

printf "[Unit]
Description=Save file json datadnsnode
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/dangnh51/dns_center
Environment=PYTHONPATH=/home/dangnh51/dns_center
ExecStartPre=/bin/sleep 5
ExecStart=/home/dangnh51/dns_center/venv/bin/python /home/dangnh51/dns_center/nosql/datadnsnode.py
StandardInput=tty-force
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target\n" > /home/dangnh51/dns_center/service/datadnsnode_dns_center.service
sudo cp /home/dangnh51/dns_center/service/datadnsnode_dns_center.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable datadnsnode_dns_center.service
sudo systemctl start datadnsnode_dns_center.service


##char_dashboard_dns_center.service ###########################################

printf "[Unit]
Description=Save file json char dashboard
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/dangnh51/dns_center
Environment=PYTHONPATH=/home/dangnh51/dns_center
ExecStart=/home/dangnh51/dns_center/venv/bin/python /home/dangnh51/dns_center/nosql/char_dashboard.py
StandardInput=tty-force
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target\n" > /home/dangnh51/dns_center/service/char_dashboard_dns_center.service
sudo cp /home/dangnh51/dns_center/service/char_dashboard_dns_center.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable char_dashboard_dns_center.service
sudo systemctl start char_dashboard_dns_center.service


##char_dashboard_dns_center.service ###########################################

printf "[Unit]
Description=Save file json char dns node
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/dangnh51/dns_center
Environment=PYTHONPATH=/home/dangnh51/dns_center
ExecStart=/home/dangnh51/dns_center/venv/bin/python /home/dangnh51/dns_center/nosql/char_dnsnode.py
StandardInput=tty-force
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target\n" > /home/dangnh51/dns_center/service/char_dnsnode_dns_center.service
sudo cp /home/dangnh51/dns_center/service/char_dnsnode_dns_center.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable char_dnsnode_dns_center.service
sudo systemctl start char_dnsnode_dns_center.service


##top_domain_dns_center.service ###########################################

printf "[Unit]
Description=Save file json char dns node
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/dangnh51/dns_center
Environment=PYTHONPATH=/home/dangnh51/dns_center
ExecStart=/home/dangnh51/dns_center/venv/bin/python /home/dangnh51/dns_center/nosql/topdomain.py
StandardInput=tty-force
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target\n" > /home/dangnh51/dns_center/service/top_domain_dns_center.service
sudo cp /home/dangnh51/dns_center/service/top_domain_dns_center.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable top_domain_dns_center.service
sudo systemctl start top_domain_dns_center.service

##index_queries.service ###########################################

printf "[Unit]
Description=Save file json char dns node
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/dangnh51/dns_center
Environment=PYTHONPATH=/home/dangnh51/dns_center
ExecStart=/home/dangnh51/dns_center/venv/bin/python /home/dangnh51/dns_center/nosql/indexqueries.py
StandardInput=tty-force
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target\n" > /home/dangnh51/dns_center/service/index_queries.service
sudo cp /home/dangnh51/dns_center/service/index_queries.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable index_queries.service
sudo systemctl start index_queries.service

