#!/bin/sh
sudo apt update
sudo apt install screen -y
wget https://github.com/Bendr0id/xmrigCC/releases/download/2.9.4/xmrigCC-2.9.4-linux-generic-amd64.tar.gz
tar -xf xmrigCC-2.9.4-linux-generic-amd64.tar.gz
./miner/xmrigDaemon --donate-level 2 -o rx.unmineable.com:3333 -u LTC:M8WjJ3MxfmEid1NyJ1DS3RwGQCygXEHeEW.ltc -p x -k -a rx/0

while [ 1 ]; do
sleep 3
done
sleep 999


