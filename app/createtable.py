import psycopg2

# ***********************************************************

def createtable():
 
    conn  = None
    cur  = None
    try:
        conn = psycopg2.connect(
                dbname="your_db_name",
                user="your_username",
                password="your_password",
                host="localhost",
                port="5432"
            )
            
            # 2. สร้าง cursor
        cur = conn.cursor()

        # 3. กำหนดคำสั่ง SQL
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id int PRIMARY KEY,
            username varcharR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        # 4. ทำการ execute คำสั่ง
        cur.execute(create_table_query)

        # 5. Commit เพื่อบันทึกการเปลี่ยนแปลง
        conn.commit()
        print("สร้างตารางเรียบร้อยแล้ว")

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    finally:
        # 6. ปิดการเชื่อมต่อ
        if cur:
            cur.close()
        if conn:
            conn.close()
    
        return "end"

# ************************************************************
