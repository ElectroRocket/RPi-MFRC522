#Author :Krishaay Jois
#Date Written: 22 December 2018
#Purpose: To install RFID and SPI libraries for MFRC522 module
cd /home/pi
#begin
echo "installation started"
sudo apt-get update
sudo apt-get upgrade -y
lsmod | grep spi
sudo apt-get install python-spidev python3-spidev
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py/
sudo python setup.py install
cd /home/pi
pwd
git clone https://github.com/ElectroRocket/RPi-MFRC522.git
cd RPi-MFRC522
echo "installation completed"

