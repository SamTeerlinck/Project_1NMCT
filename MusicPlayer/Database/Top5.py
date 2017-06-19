"""
Project
Sam Teerlinck
1NMCT4
"""

import MySQLdb		#connection with database

#connect with database
db = MySQLdb.connect("localhost", "samteerlinck", "password", "musicplayer")
curs=db.cursor()

i=0

curs.execute ("SELECT TOP 5 type, COUNT(songname) Total FROM played GROUP BY type ORDER BY total DESC")

print "\nNr.     	Song Name"
print "============================"

for reading in curs.fetchall():
    print i+"	"+str(reading[0])
	i += 1
	if i == 6:
	break