#install script v0.1

#!/bin/bash -e
# apt-get update
/usr/bin/sudo apt-get update

# apt-get upgrade
/usr/bin/sudo apt-get -y upgrade

# RPI update
/usr/bin/sudo rpi-update

# reboot

# install dependencies
apt-get install sqlite3 git

git clone https://github.com/max4260/webiopi.git
#https://code.google.com/p/webiopi

#auto start webiopi on boot

#configure sqlite3
