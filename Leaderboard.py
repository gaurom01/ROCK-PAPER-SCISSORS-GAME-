import mysql.connector

# Database connection details
db_config = {
    "host": "localhost",          # Replace with your host
    "user": "root",      # Replace with your username
    "password": "root",  # Replace with your password
    "database": "gamescores"   # Replace with your database name
}

try:
    # Establish the connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Query to fetch the required columns
    query = """
    SELECT player_name, player_score, computer_score, result
    FROM gameresults;
    """
    
    # Execute the query
    cursor.execute(query)
    rows = cursor.fetchall()

    # Print the results
    print(f"{'Player Name':<20}{'Player Score':<15}{'Computer Score':<15}{'Result':<10}")
    print("-" * 60)
    
    for row in rows:
        print(f"{row[0]:<20}{row[1]:<15}{row[2]:<15}{row[3]:<10}")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Clean up and close the connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()