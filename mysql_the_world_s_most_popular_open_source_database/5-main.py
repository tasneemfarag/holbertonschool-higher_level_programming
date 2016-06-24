import mysql.connector

cnx = mysql.connector.connect(user='student', password='aLQQLXGQp2rJ4Wy5',host='173.246.108.142',database='Project_169')
cursor = cnx.cursor()

query = ("SELECT TVShow.name, Season.number, Episode.number, Episode.name FROM TVShow, Season, Episode WHERE Season.id = Episode.season_id AND TVShow.id = Season.tvshow_id ORDER BY TVShow.name, Season.number, Episode.number")

cursor.execute(query)
result = cursor.fetchall() 
TVShowName = []
SeasonNumber = []
for row in result:
	if row[0] not in TVShowName:		
  		print row[0] + ":"
  		TVShowName.append(row[0])
  		SeasonNumber = []
  	if row[1] not in SeasonNumber:		
  		print "\tSeason " + str(row[1]) + ":"
  		SeasonNumber.append(row[1])	
  	print "\t\t" + str(row[2]) + ": " + row[3]

cursor.close()
cnx.close()