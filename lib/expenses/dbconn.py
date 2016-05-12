import psycopg2
import os

def get():
    return psycopg2.connect(
        database='expenses',
        user='postgres',
        password='postgres',
        host='localhost'
    )
