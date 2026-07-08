import psycopg2

# ***********************************************************

def insertdata_customer():

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
        
 
        cursor = conn.cursor()


        customername =   "AAA"
        taxid  = "0122222366632"
        address = "123  sukhumwit rd. 10110"
        phone  = "0885555555"
        status = '1'
    
        
  
        sql_query = "INSERT INTO customer  ( customername, taxid , address ,phone ,status ) VALUES (%s , %s , %s , %s , %s  ) ; "

 
        cursor.execute(sql_query, ( customername, taxid , address ,phone ,status  ))
    
        conn.commit()  
 

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
 
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    
        return "end"



