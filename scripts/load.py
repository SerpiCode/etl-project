import mysql.connector
import mysql.connector.cursor
import pandas as pd
import os

def connect_to_mysql(host, port, user, password, db):
    '''Establish connection to mySQL.'''
    try:
        connection = mysql.connector.connect(host=host,
                                             port=port,
                                             user=user,
                                             password=password,
                                             database=db)
        print('Connection to mySQL established.')
        return connection
    except mysql.connector.Error as e:
        print(f'MySQL connection error: {e}')
        return None
    
def map_dtype_to_mysql(dtype):
    '''Maps all data types from Pandas to SQL'''
    if pd.api.types.is_integer_dtype(dtype):
        return "INT"
    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "DATETIME"
    elif pd.api.types.is_string_dtype(dtype):
        return "TEXT"
    else:
        return "TEXT"
    
def create_table_from_dataframe(connection, table_name, df):
    '''Creates SQL table based on a DataFrame'''
    cursor = connection.cursor()

    # Generate SQL query
    columns = []
    for col, dtype in zip(df.columns, df.dtypes):
        mysql_dtype = map_dtype_to_mysql(dtype)
        columns.append(f"`{col}` {mysql_dtype}")
    columns_sql = ', '.join(columns)

    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql});"

    try:
        cursor.execute(create_table_query)
        print(f"Table {table_name} successfully created.")
    except mysql.connector.Error as e:
        print(f"Error - could not create table {table_name}: {e}")
    finally:
        cursor.close()

def load_data_to_mysql(connection, table_name, data_path):
    '''Loads CSV data to MySQL'''
    try:
        df = pd.read_csv(data_path)
        print(f"{len(df)} lines will be loaded into {table_name} table.")

        create_table_from_dataframe(connection, table_name, df)
        cursor = connection.cursor()

        for _, row in df.iterrows():
            query = f"""
            INSERT INTO {table_name} ({', '.join(df.columns)})
            VALUES ({', '.join(['%s'] * len(df.columns))});
            """
            cursor.execute(query, tuple(row))

        connection.commit()
        print("Data successfully loaded into mySQL.")
    except Exception as e:
        print(f"Error loading data: {e}")
    finally:
        cursor.close()

if __name__ == '__main__':
    # Settings
    host = "localhost"
    port = "3307"
    user = "root"
    password = "root"
    database = "etl_project"
    table_name = "netflix_titles"
    data_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'netflix_titles_cleaned.csv')

    # Connect to mySQL
    connection = connect_to_mysql(host, port, user, password, database)
    if connection:
        # Load data
        load_data_to_mysql(connection, table_name, data_path)
        connection.close()