import mysql.connector

cnx = mysql.connector.connect(user='student', password='aLQQLXGQp2rJ4Wy5',host='173.246.108.142',database='Project_169')
cursor = cnx.cursor()

query = ("SHOW tables")

cursor.execute(query)

for table in cursor:
  print "" + table

cursor.close()
cnx.close()