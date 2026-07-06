import psycopg2

# ***********************************************************

def createtable():
 
    connection = None
    cursor = None
    try:
        # 1. Connect to your PostgreSQL database
        connection = psycopg2.connect(
            user="myuser",
            password="mypassword",
            host="localhost",
            port="5432",
            database="mydatabase"
        )
        
        # 2. Create a cursor object
        cursor = connection.cursor()
        
        # 3. Define the SQL Query for table creation
        create_table_query = '''

            CREATE TABLE IF NOT EXISTS customer (
                cid SERIAL PRIMARY KEY,
                customername VARCHAR(100) ,
                taxid VARCHAR(13) ,
                address VARCHAR(250) ,
                phone VARCHAR(50) ,
                status VARCHAR(1) ,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
                '''

        
        
        # 4. Execute the SQL command
        cursor.execute(create_table_query)
        
        # 5. Commit the transaction to save changes
        connection.commit()
        print("Table 'customer' created successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL or creating table:", error)
        if connection:
            # Rollback the transaction in case of an error
            connection.rollback()

    finally:
        # 6. Turn off communication with the database safely
        if cursor:
            cursor.close()
        if connection:
            connection.close()
 
    return "Table Created Successfully"

# ************************************************************
