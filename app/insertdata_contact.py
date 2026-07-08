import psycopg2

# ***********************************************************

def insertdata_contact():

    conn  = None
    cursor = None
    try:
        conn = psycopg2.connect(
                dbname="mydatabase",
                user="myuser",
                password="mypassword",
                host="dbpg",
                port="5432"
            )
        
 
        contactdetail = "Test Contact info" 
        cid = 1
        status = '1' 
        submitdate = '01/07/2026'
        submittime = '10:10:10'  

        cursor = conn.cursor()
        sql_query = "INSERT INTO contact  ( contactdetail , cid, status , submitdate , submittime ) VALUES (%s , %s, %s , %s , %s  ) ; "
        cursor.execute(sql_query, ( contactdetail , cid, status , submitdate , submittime  ))
        conn.commit()  

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
 
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    
        return "end"



