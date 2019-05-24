from DB.connection import Connection
from Utils.utils import get_select_query, get_insert_query
import pymysql


def execute_select(columns, table, where_columns=None, where_values=None):
    try:
        with Connection.mysql.get_db().cursor() as cursor:
            if where_columns is None and where_values is None:
                query = get_select_query(columns, table)
                cursor.execute(query)
            else:
                query = get_select_query(columns, table, where_columns)
                cursor.execute(query, where_values)
            data = cursor.fetchall()
            return data
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return ()
    finally:
        cursor.close()


def execute_insert(columns, table, values):
    try:
        with Connection.mysql.get_db().cursor() as cursor:
            query = get_insert_query(columns, table)
            cursor.execute(query, values)
            # Insertar commit
            return data
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return ()
    finally:
        cursor.close()
