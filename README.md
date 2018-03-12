
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
<CODE>
<BR>
pip3 install PyQt5
<BR>
pip3 install pySerial
<BR>
pip3 install mysqlclient pymysql
<BR>
echo "import pymysql" > manage.py
<BR>
echo "pymysql.install_as_MySQLdb()" >> manage.py
<BR>
pip3 install queuelib
<BR>
</CODE>
For Linux, you have to install Python3, Qt5 and mysql database
<BR>
On the MySql server, you have to add a user "Chrono", password "Chrono"
with dba right.
<BR>
Then execute the sql script to create the table and fill it with some datas:
<BR>
schema.sql			this create the tables
<BR>
iso_pays.sql			fill the T_Pays tables with iso Country code
<BR>
CodepostaleSuisse.sql 	fill the zip/city table ( actually only CH )
<BR>
all this file are mandarory !
<BR>
the test_data.sql are some data to test.....
<BR>
Thor
<BR>
For the decoder and transponder watch this link:
<BR>
<a href="https://www.rctech.net/forum/radio-electronics/1002584-rchourglass-diy-lap-timing-aka-cano-revised-11.html">
RCHourglass Transponder
</a>
<BR>
and the repository for the software and schematic:
<BR>
<a href="https://github.com/mv4wd/RCHourglass">mv4wd Decoder / Transponder</a>
