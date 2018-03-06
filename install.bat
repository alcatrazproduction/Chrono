pip3 install PyQt5
pip3 install serial
pip3 install mysqlclient pymysql
echo "import pymysql" > manage.py
echo "pymysql.install_as_MySQLdb()" >> manage.py
pip3 install queuelib
