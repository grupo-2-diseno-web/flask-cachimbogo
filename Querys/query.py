from DB.connection import Connection
from pymysql import Error


class Query(object):

    def get_cursor(self):
        return Connection.mysql.get_db().cursor()

    def execute_select(self, columns, table, where_columns=None, where_values=None):
        try:
            with self.get_cursor() as cursor:
                if where_columns is None and where_values is None:
                    query = self.get_select_query(columns, table)
                    cursor.execute(query)
                else:
                    query = self.get_select_query(
                        columns, table, where_columns)
                    cursor.execute(query, where_values)
                data = cursor.fetchall()
                return data
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            return []
        finally:
            cursor.close()

    def execute_insert(self, columns, table, values):
        try:
            with self.get_cursor() as cursor:
                query = self.get_insert_query(columns, table)
                cursor.execute(query, values)
                # Insertar commit
                cursor.connection.commit()
                return True
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            cursor.connection.rollback()
            return False
        finally:
            cursor.close()

    def execute_update(self, columns, table, values, where_columns=None, where_values=None):
        try:
            with self.get_cursor() as cursor:
                if where_columns is None and where_values is None:
                    query = self.get_update_query(columns, table)
                    cursor.execute(query, values)
                else:
                    query = self.get_update_query(
                        columns, table, where_columns)
                    cursor.execute(query, values + where_values)
                cursor.connection.commit()
                return True
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            cursor.connection.rollback()
            return False
        finally:
            cursor.close()

    def execute_delete(self, table, where_columns=None, where_values=None):
        try:
            with self.get_cursor() as cursor:
                if where_columns is None and where_values is None:
                    query = self.get_delete_query(table)
                    cursor.execute(query)
                else:
                    query = self.get_delete_query(table, where_columns)
                    cursor.execute(query, where_values)
                cursor.connection.commit()
                return True
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            cursor.connection.rollback()
            return False
        finally:
            cursor.close()

    def execute_join(self, join_query, where_values=None):
        try:
            with self.get_cursor() as cursor:
                if where_values is None:
                    cursor.execute(join_query)
                else:
                    cursor.execute(join_query, where_values)
                data = cursor.fetchall()
                return data
        except Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            return []
        finally:
            cursor.close()

    @staticmethod
    def get_select_query(columns, table, where_columns=None):
        query = "SELECT "
        i = 0
        length = len(columns)
        while length - 1 > i:
            query += columns[i] + ", "
            i += 1
        query += columns[i] + " FROM " + table
        if where_columns is None:
            query += ";"
        else:
            length = len(where_columns)
            i = 0
            query += " WHERE "
            while length - 1 > i:
                query += where_columns[i] + " = %s, "
                i += 1
            query += where_columns[i] + " = %s;"
        return query

    @staticmethod
    def get_insert_query(columns, table):
        query = "INSERT INTO " + table + "("
        i = 0
        length = len(columns)
        while length - 1 > i:
            query += columns[i] + ", "
            i += 1
        query += columns[i] + ") VALUES ("
        i = 0
        length = len(columns)
        while length - 1 > i:
            query += "%s, "
            i += 1
        query += "%s);"
        return query

    @staticmethod
    def get_update_query(columns, table, where_columns=None):
        query = "UPDATE " + table + " SET "
        i = 0
        length = len(columns)
        while length - 1 > i:
            query += columns[i] + " = %s, "
            i += 1
        query += columns[i] + " = %s"
        if where_columns is None:
            query += ";"
        else:
            length = len(where_columns)
            i = 0
            query += " WHERE "
            while length - 1 > i:
                query += where_columns[i] + " = %s, "
                i += 1
            query += where_columns[i] + " = %s;"
        return query

    @staticmethod
    def get_delete_query(table, where_columns=None):
        query = "DELETE FROM " + table
        if where_columns is None:
            query += ";"
        else:
            length = len(where_columns)
            i = 0
            query += " WHERE "
            while length - 1 > i:
                query += where_columns[i] + " = %s, "
                i += 1
            query += where_columns[i] + " = %s;"
        return query
