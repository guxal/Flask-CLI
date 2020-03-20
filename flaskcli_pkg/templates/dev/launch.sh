#!/bin/bash
kill -9 `cat api.pid` > /dev/null 2>&1;
kill -9 `cat web.pid` > /dev/null 2>&1;
sleep 2;

<[app]>_MYSQL_USER=<[app-lower]>_dev \
<[app]>_MYSQL_PWD=<[app-lower]>_dev_pwd \
<[app]>_MYSQL_HOST=localhost \
<[app]>_MYSQL_DB=<[app-lower]>_dev_db \
<[app]>_TYPE_STORAGE=db \
<[app]>_API_HOST=0.0.0.0 \
<[app]>_API_PORT=5000 \
# this display logs in the file and reload the new code write
<[app]>_API_DEBUG=True \
<[app]>_API_THREAD=True \
# enviroment test drop database in each init
<[app]>_ENV=test \

python3 -m api.v1.app > ./dev/api.log 2>&1 &
echo $! > api.pid

<[app]>_FRONT_DEBUG=True \
<[app]>_FRONT_THREAD=True \
<[app]>_FRONT_HOST=0.0.0.0 \
<[app]>_FRONT_PORT=5001 \

python3 -m web.app > ./dev/web.log 2>&1 &
echo $! > web.pid


sleep 5;
