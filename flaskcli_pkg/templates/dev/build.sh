#!/bin/bash
# This script build enviroments
sudo find . -name "*.py" -exec chmod u+x {} \;
sudo find . -name "*.sh" -exec chmod u+x {} \;
sudo ./dev/./setup_local_server.sh
source ./dev/./export_fc_var.sh
cat ./dev/setup_mysql_test.sql | sudo mysql
cat ./dev/setup_mysql_dev.sql | sudo mysql
sudo pip3 install -r ./dev/requirements.txt
