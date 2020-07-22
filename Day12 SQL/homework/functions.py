from psycopg2.extras import DictCursor
import psycopg2


def connect():
    try:
        connect = psycopg2.connect(dbname='products', user='postgres',
                                   password='postgres', host='localhost', port=5432)
        return connect
    except:
        print('Ошибка открытия БД.')


def reading():
    cursor = connect().cursor()
    cursor.execute('SELECT * FROM products')
    data = cursor.fetchall()
    for i in data:
        print(i)


def add_in_db(n, p, a, c):
    conn = connect()
    cursor = conn.cursor()
    try:
        inner = ("""INSERT INTO products (name, price, amount, comment) values ('%s','%d','%d','%s')""" % (n, p, a, c))
        cursor.execute(inner)
        conn.commit()
        print(f"Товар {n} добавлен успешно.")
    except:
        conn.rollback()
        print('Ошибка добавления.')
    conn.close()


# add_in_db('nam',24,76,'azaza')

def deleter_by_id(id):
    conn = connect()
    cursor = conn.cursor()
    try:
        deleter = """
                    DELETE FROM products WHERE id = '%d'
                    """ % (id)
        cursor.execute(deleter)
        conn.commit()
        print(f'Товар с id {id} удален.')
    except:
        conn.rollback()
        print(f'Ошибка при удалении товара.')
    conn.close()


def updater_by_id(id, name_column, new_data):
    conn = connect()
    cursor = conn.cursor()
    if new_data == 'name' or new_data == 'comment':
        updater = """
                    UPDATE products SET %'s'=name_column
        """
    else:
        updater = """
                    UPDATE products SET name_column = '%d'
                """ % (new_data)
