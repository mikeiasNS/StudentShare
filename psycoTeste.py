import psycopg2

try:
	conn = psycopg2.connect("dbname='StudantShareDB' user='postgres' password='postgres' host='localhost' port='5433'")
	print "uhu \o/"
except:
    print "ieieieie"
