import psycopg2

def dbconn():
    conn = None  # กำหนดค่าเริ่มต้นไว้ก่อน
    try:
        conn = psycopg2.connect(
            host="dbpg",
            database="mydatabase",
            user="myuser",
            password="mypassword",
            port="5432"
        )
        print("Database's Connected")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    
    return conn  # ถ้าต่อไม่ได้ จะคืนค่า None ออกไป