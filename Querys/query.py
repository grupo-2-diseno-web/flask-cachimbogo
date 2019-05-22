from DB.connection import Connection
from Utils.utils import get_select_query
import pymysql


def execute_select(columns, table, where_columns, where_values):
    try:
        with Connection.mysql.get_db().cursor() as cursor:
            query = get_select_query(columns, table,
                                     where_columns)
            cursor.execute(query, where_values)
            data = cursor.fetchall()
            return data
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        return ()
    finally:
        cursor.close()
