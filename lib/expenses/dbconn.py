import psycopg2
import os

def get():
    return psycopg2.connect(
        database=os.environ['PGDATABASE'],
        user=os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
        password=os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
        host=os.environ['OPENSHIFT_POSTGRESQL_DB_HOST']
    )
