import csv
import googlemaps

csvinput = open('mines.csv', 'rb')
csvoutput = open('mines_geo.csv', 'wb')

rows = []
r = csv.reader(csvinput, delimiter=',')
for row in r:
	print(row)
