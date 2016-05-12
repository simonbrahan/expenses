import psycopg2


def get():
    return psycopg2.connect(
        database='expenses',
        user='postgres',
        password='postgres',
        host='localhost'
    )
