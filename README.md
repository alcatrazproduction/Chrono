
# Chrono
$VERS: 0.1alpha

Software to race timing wrtiten in Python/Qt5

For Windows install:
You must install Python3
<BR>
<a href="https://www.python.org/downloads/windows/">
Python 3 Download
</a>
<BR>
MysqlServer
<BR>
<a href="https://dev.mysql.com/downloads/installer/">
MysqlServer Download
</a>
<BR>
then install all the Python stuff with the install.bat script

pip3 install PyQt5
pip3 install pySerial
pip3 install mysqlclient pymysql
echo "import pymysql" > manage.py
echo "pymysql.install_as_MySQLdb()" >> manage.py
pip3 install queuelib

For Linux, you have to install Python3, Qt5 and mysql database

On the MySql server, you have to add a user "Chrono", password "Chrono"
with dba right.
Then execute the sql script to create the table and fill it with some datas:
schema.sql			this create the tables
iso_pays.sql			fill the T_Pays tables with iso Country code
CodepostaleSuisse.sql 	fill the zip/city table ( actually only CH )
all this file are mandarory !

the test_data.sql are some data to test.....

Thor

For the decoder and transponder watch this link:
<BR>
<a href="https://www.rctech.net/forum/radio-electronics/1002584-rchourglass-diy-lap-timing-aka-cano-revised-11.html">
RCHourglass Transponder
</a>
<BR>
and the repository for the software and schematic:
<BR>
<a href="https://github.com/mv4wd/RCHourglass">mv4wd Decoder / Transponder</a>
