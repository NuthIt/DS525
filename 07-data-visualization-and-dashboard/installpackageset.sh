sudo apt-get update
sudo apt install python3-pip -y
sudo apt-get install libpq-dev python3-dev -y
pip3 install numpy
pip3 install pandas
pip3 install boto3
pip3 install psycopg2

echo "*/15 * * * * /usr/bin/python3 /home/$USER/etl.py" | crontab -

sudo reboot