import psycopg2

# ***********************************************************

def createtable_contact():
 
    conn  = None
    cursor  = None
    try:
        conn = psycopg2.connect(
                dbname="mydatabase",
                user="myuser",
                password="mypassword",
                host="dbpg",
                port="5432"
            )
            
 
        cursor = conn.cursor()

 
        create_table_query = """
        CREATE TABLE IF NOT EXISTS contact (
            conid serial primary key NOT NULL ,
            contactdetail text ,
            cid bigint ,
            status text ,
            submitdate text ,
            submittime text
        );
        """

        cursor.execute(create_table_query)
   
        conn.commit()
 

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
 
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    
        return "end"

# ************************************************************
