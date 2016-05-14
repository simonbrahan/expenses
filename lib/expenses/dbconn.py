import psycopg2

__DBNAME__ = None
__DBUSERNAME__ = None
__DBPASSWORD__ = None
__DBHOST__ = None

def init(environ):
    global __DBNAME__
    global __DBUSERNAME__
    global __DBPASSWORD__
    global __DBHOST__

    __DBNAME__ = environ['PGDATABASE']
    __DBUSERNAME__ = environ['OPENSHIFT_POSTGRESQL_DB_USERNAME']
    __DBPASSWORD__ = environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD']
    __DBHOST__ = environ['OPENSHIFT_POSTGRESQL_DB_HOST']

def get():
    global __DBNAME__
    global __DBUSERNAME__
    global __DBPASSWORD__
    global __DBHOST__

    return psycopg2.connect(
        database = __DBNAME__,
        user = __DBUSERNAME__,
        password = __DBPASSWORD__,
        host = __DBHOST__
    )
