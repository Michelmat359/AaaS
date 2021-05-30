#!/bin/bash

set -m

# start redis
echo " --- Starting redis --- "
service redis-server start 

# start mongo 
#service mongod start 
echo " --- Starting mongoDB --- "
/usr/bin/mongod --config /etc/mongod.conf &
#service mongod status

