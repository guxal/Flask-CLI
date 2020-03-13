#!/bin/bash
# various bash commands to setup local environment
# TODO: create setup script or Docker Container that has these configurations
# Make it happen!
wget http://dev.mysql.com/get/mysql-apt-config_0.6.0-1_all.deb
dpkg -i mysql-apt-config_0.6.0-1_all.deb
apt-get update
apt-get install -y mysql-server
rm mysql-apt-config_0.6.0-1_all.deb
apt-get install -y python3-dev libmysqlclient-dev
service mysql start
