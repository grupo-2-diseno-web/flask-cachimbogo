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
        return []
    finally:
        cursor.close()


def execute_insert(columns, table, values):
    try:
        with Connection.mysql.get_db().cursor() as cursor:
            query = get_insert_query(columns, table)
            cursor.execute(query, values)
            # Insertar commit
            cursor.connection.commit()
            return True
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        cursor.connection.rollback()
        return False
    finally:
        cursor.close()


def execute_join(join_query, where_values=None):
    try:
        with Connection.mysql.get_db().cursor() as cursor:
            if where_values is None:
                cursor.execute(join_query)
            else:
                cursor.execute(join_query, where_values)
            data = cursor.fetchall()
            return data
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return []
    finally:
        cursor.close()


def execute_insert_into(insert_into_query, where_values=None):
    try:
        with Connection.mysql.get_db().cursor() as cursor:
            cursor.execute(insert_into_query, where_values)
            # Insertar commit
            cursor.connection.commit()
            return True
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        cursor.connection.rollback()
        return False
    finally:
        cursor.close()
