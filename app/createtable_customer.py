import psycopg2

# ***********************************************************

def createtable_customer():
 
    conn  = None
    cur  = None
    try:
        conn = psycopg2.connect(
                dbname="mydatabase",
                user="myuser",
                password="mypassword",
                host="dbpg",
                port="5432"
            )
            
 
        cur = conn.cursor()

 
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customer (
            cid serial primary key not null ,
            customername text ,
            taxid  text  ,
            address text  ,
            phone  text,
            status text
        );
        """


 
        cur.execute(create_table_query)

 
        conn.commit()
 

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
 
        if cur:
            cur.close()
        if conn:
            conn.close()
    
        return "end"

# ************************************************************
