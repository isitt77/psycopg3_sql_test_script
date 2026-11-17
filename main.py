import psycopg as pg3

conn = pg3.connect(dbname='dvdrental',user='postgres')

cur=conn.cursor()

cur.execute('SELECT * FROM film')
row = cur.fetchmany(3)
print(row[2])

cur.close()
conn.close()