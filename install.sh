#!/usr/bin/env bash

# Install script

apt-get update
apt-get install virtualenv

sudo mkdir -p /app/eventtime-client
sudo chown -R pi:pi /app
cp eventtime-client-scrollphathd.py /app/eventtime-client
virtualenv -p python3 /app/eventtime-client/venv
. /app/eventtime-client/venv/bin/activate
pip install -r requirements

sudo cp library/eventtime-client.service /lib/systemd/system/eventtime-client.service
sudo chmod 644 /lib/systemd/system/eventtime-client.service
sudo systemctl daemon-reload
sudo systemctl enable eventtime-client.service

echo "Use: systemctl start eventtime-client.service"