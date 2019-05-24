import configparser
import hashlib


def get_config():
    config_parser = configparser.RawConfigParser()
    config_file_path = r'Utils/config.txt'
    config_parser.read(config_file_path)
    return config_parser


def get_crypt(word):
    h256 = hashlib.sha256()
    h256.update(word.encode())
    word_hash = h256.hexdigest()
    return word_hash


def get_delete_query(table, where_columns = None):
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


def get_update_query(columns, table, where_columns = None):
    query = "UPDATE " + table + " SET "
    i = 0
    length = len(columns)
    while length -1 > i:
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


def get_insert_query(columns,table):
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


def get_select_query(columns, table, where_columns = None):
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


def build_response(names, array_values):
    if len(array_values) is 0:
        return None
    elif len(array_values) is 1:
        return build_dictionary(names, array_values[0])
    else:
        array_data = []
        for values in array_values:
            array_data.append(build_dictionary(names, values))
        return array_data


def build_dictionary(names, array_values):
    data = {}
    i = 0
    length = len(names)
    while length > i:
        data[names[i]] = array_values[i]
        i += 1
    return data
