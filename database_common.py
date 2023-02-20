import psycopg2
import psycopg2.extras


def get_connection_string():
    # /TODO: Hide sensitive data
    return ("dbname=super_sprinter user=postgres password=Bulbulator1337")


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        cur = connection.cursor()
        ret_value = function(cur, *args, **kwargs)
        connection.commit()
        cur.close()
        connection.close()
        return ret_value
    return wrapper
