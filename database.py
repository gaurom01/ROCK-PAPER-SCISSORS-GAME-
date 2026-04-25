import mysql.connector
from mysql.connector import Error
from datetime import datetime

def create_database(cursor, db_name):
    """Create a database if it does not exist."""
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' created or already exists.")
    except Error as e:
        print(f"Error creating database: {e}")

def create_table(conn, table_name):
    """Create a table in the specified database."""
    try:
        cursor = conn.cursor()
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            player_name VARCHAR(100) NOT NULL,
            player_score INT NOT NULL,
            computer_score INT NOT NULL,
            result VARCHAR(50) NOT NULL,
            game_date DATETIME NOT NULL
        )
        """
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created or already exists.")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_entry(conn, table_name, player_name, player_score, computer_score, result):
    """Insert a new entry into the table."""
    try:
        cursor = conn.cursor()
        insert_query = f"""
        INSERT INTO {table_name} (player_name, player_score, computer_score, result, game_date)
        VALUES (%s, %s, %s, %s, %s)
        """
        game_date = datetime.now()
        cursor.execute(insert_query, (player_name, player_score, computer_score, result, game_date))
        conn.commit()
        print("Entry added successfully.")
    except Error as e:
        print(f"Error inserting entry: {e}")


    """Setup database, table, and add initial entries."""
try:
       # Connect to MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    if conn.is_connected():
        print("Connection established...")
        cursor = conn.cursor()

        # Database and table setup
        database_name = "GameScores"
        table_name = "GameResults"
        create_database(cursor, database_name)

            # Use the newly created database
        conn.database = database_name
        create_table(conn, table_name)

            # Add entries using the function

except Error as e:
    print(f"Connection error: {e}")



