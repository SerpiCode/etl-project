import mysql.connector
import pandas as pd
import os

db_info = {'host': 'localhost',
           'user': 'root',
           'password': 'root',
           'db': 'etl_project',
           'port': 3307}

def fetch_data(query):
    connection = mysql.connector.connect(
        host = db_info['host'],
        user = db_info['user'],
        password = db_info['password'],
        database = db_info['db'],
        port = db_info['port']
    )

    try:
        df = pd.read_sql(query, connection)
    finally:
        connection.close()

    return df

def load_query(identifier, file_path='scripts/queries.sql'):
    with open(file_path, 'r') as file:
        queries = file.read()
    
    identifier_tag = f"-- {identifier}"
    if identifier_tag not in queries:
        raise ValueError(f"Query '{identifier}' not found in {file_path}.")
    
    queries_split = queries.split(identifier_tag)
    query_block = queries_split[1].split('--')[0]

    return query_block.strip()

# if __name__ == '__main__':
#     path = os.path.join(os.path.dirname(os.getcwd()), 'scripts', 'queries.sql')
    
#     query = load_query("QUERY_TITLES_BY_RATING", path)
#     df = fetch_data(query)
    
#     print(df.head())