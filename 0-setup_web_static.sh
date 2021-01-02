#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
apt-get update && apt-get -y install nginx
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-enabled/default
sudo service nginx restart
