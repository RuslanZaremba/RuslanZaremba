import psycopg2
from contextlib import closing

connect = psycopg2.connect(dbname='products', user='postgres',
                           password='postgres', host='localhost', port=5432)

cursor = connect.cursor()

cursor.execute("insert into products (name, price, amount, comment) values ('MacBook', 1000, 10, 'new power laptop')")
# cursor.execute("TRUNCATE TABLE products")
connect.commit()




