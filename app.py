from flask import Flask, render_template, request, redirect , url_for
import psycopg2  # อย่าลืม import ไลบรารีนี้ครับ
from app.connectdb import dbconn

from app.createtable import createtable


from datetime import datetime

app = Flask(__name__)
 
 
 

# ************************************************************

@app.route("/createtable")
def createdata():
    return createtable()




@app.route("/")
def selectdata():
    customers = []
    try:
        conn = dbconn()
        cursor = conn.cursor()
        cursor.execute("SELECT cid, customername, taxid, address , phone FROM customer  where status like '1'  order by cid asc;")
        customers  = cursor.fetchall()
        # --- เพิ่มบรรทัดนี้เพื่อเช็คข้อมูล ---
        print("DEBUG: ข้อมูลที่ได้จาก DB คือ:", customers)
        # ---------------------------------
        cursor.close()
        conn.close()

        
    except Exception as e:
        print( "Query Operation Error")

    return render_template("customer.html"  , rows=customers)

# ************************************************************

@app.route('/customers/addnewcustomer')
def addnewcustomer():    
    return render_template('addnewform.html')



# ************************************************************
@app.route("/customers/insert" , methods=['GET', 'POST']  )
def insertcustomery():
    if request.method == 'POST':
    # 1. รับค่าจากฟอร์ม HTML

        customername = request.form.get('customername')
        taxid = request.form.get('taxid')
        address = request.form.get('address')        
        phone = request.form.get('phone')
    
        # 2. 🌟 คำสั่งสำหรับ PostgreSQL
        conn = dbconn()
        cursor = conn.cursor()
        
        sql_query = "INSERT INTO customer ( customername,taxid,address,phone,status) VALUES (%s, %s, %s, %s ,%s) ; "
    
        # รันคำสั่ง SQL
        cursor.execute(sql_query, (customername,taxid,address,phone,'1'))
        
        conn.commit()  # บันทึกข้อมูล
        cursor.close() # ปิด cursor
        conn.close()   # ปิดการเชื่อมต่อ
        
        # 3. รีไดเรกต์กลับไปหน้าแรก (Root)
    return redirect('/')







# ************************************************************

@app.route("/customers")
def listcompany():
    customers = []
    try:
        conn = dbconn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer where status like '1'  ;")
        customers  = cursor.fetchall()
        # --- เพิ่มบรรทัดนี้เพื่อเช็คข้อมูล ---
        print("DEBUG: ข้อมูลที่ได้จาก DB คือ:", customers)
        # ---------------------------------
        cursor.close()
        conn.close()
    except Exception as e:
        print( "Query Operation Error")

    return render_template("listcompany.html"  , rows=customers)
 
# ************************************************************

@app.route("/customers/edit/<int:cid>")
def editcompany( cid ):

    customers = []

    cusid = str(cid) 
    
    try:
        conn = dbconn()
        cursor = conn.cursor()
        sqlstr = "SELECT * FROM customer where cid = '" + cusid + "'  ;"
        cursor.execute(sqlstr)
        customers  = cursor.fetchall()
 
        cursor.close()
        conn.close()
    except Exception as e:
        print( "Query Operation Error")

    return render_template("editcustomer.html"  , rows=customers)


# ************************************************************

@app.route('/customers/update/<int:cid>', methods=['GET', 'POST']  )
def updatecompany( cid ):

    #cuid = request.form.get(cid)
    cusid = str(cid)
    customername = request.form.get('customername')
    taxid        = request.form.get('taxid')
    address      = request.form.get('address')
    phone        = request.form.get('phone')

    sql_query = """
            UPDATE customer 
            SET customername = %s , taxid = %s, address = %s, phone  = %s 
            WHERE cid = %s
        """
        
        # 3. รันคำสั่ง SQL บันทึกลงฐานข้อมูล
    conn = dbconn()
    cursor = conn.cursor()


    cursor.execute(sql_query, ( customername , taxid , address , phone ,cusid))
    conn.commit()
 
    return redirect('/')

# ************************************************************
 


@app.route("/customers/delete/<int:cid>")
def deletecompany( cid ):

    customers = []

    cusid = str(cid) 
    
    try:
        conn = dbconn()
        cursor = conn.cursor()
        sqlstr = "SELECT * FROM customer where cid = '" + cusid + "'  ;"
        cursor.execute(sqlstr)
        customers  = cursor.fetchall()
 
        cursor.close()
        conn.close()
    except Exception as e:
        print( "Query Operation Error")

    return render_template("deletecustomer.html"  , rows=customers)



# ************************************************************

@app.route('/customers/deleteconfirm/<int:cid>', methods=['GET', 'POST']  )
def deletecuctomerconfirm( cid ):

    #cuid = request.form.get(cid)
    cusid = str(cid)
 
    sql_query = """
            UPDATE customer 
            SET status = %s
            WHERE cid = %s
        """
        
        # 3. รันคำสั่ง SQL บันทึกลงฐานข้อมูล
    conn = dbconn()
    cursor = conn.cursor()
    cursor.execute(sql_query, ( '0' , cusid))
    conn.commit()
 
 
    return redirect('/')

# ************************************************************


@app.route('/contactnotes')
def addnewcontactform():    
    customers = []
    try:
        conn = dbconn()
        cursor = conn.cursor()
        cursor.execute("SELECT cid , customername  FROM customer where status like '1' order by customername asc ;")
        customers  = cursor.fetchall()
        # --- เพิ่มบรรทัดนี้เพื่อเช็คข้อมูล ---
        print("DEBUG: ข้อมูลที่ได้จาก DB คือ:", customers)
        # ---------------------------------
        cursor.close()
        conn.close()
    except Exception as e:
        print( "Query Operation Error")

    return render_template("addnewcontactform.html"  , rows=customers)


# ************************************************************


@app.route('/contactnotes/addnewcontact'  , methods=['GET', 'POST']  )
def addnewcontact():    

    if request.method == 'POST':
    # 1. รับค่าจากฟอร์ม HTML
        cid = request.form.get('cid')
        contactdetail = request.form.get('contactnotes')

        dotimenow = datetime.now()
        do_date = dotimenow.strftime("%d/%m/%Y")
        do_time = dotimenow.strftime("%H:%M:%S")

        status = "1" 
        # 2. 🌟 คำสั่งสำหรับ PostgreSQL
        conn = dbconn()
        cursor = conn.cursor()
        
        sql_query = "INSERT INTO contact ( contactdetail,cid,status , submitdate ,submittime) VALUES (%s, %s, %s, %s, %s) ; "
    
        # รันคำสั่ง SQL
        cursor.execute(sql_query, ( contactdetail , cid , status , do_date, do_time ))
        
        conn.commit()  # บันทึกข้อมูล
        cursor.close() # ปิด cursor
        conn.close()   # ปิดการเชื่อมต่อ
        
        # 3. รีไดเรกต์กลับไปหน้าแรก (Root)
    return redirect('/')



# ************************************************************

@app.route('/showcontactnotes' , methods=['GET', 'POST']   )
def searchcontact():  
         
    cusname = request.values.get('cusname'  )
    customers = []
    try:
        conn = dbconn()
        cursor = conn.cursor()
        sqlstr = """
            SELECT cid, customername, address, phone 
            FROM customer 
            WHERE status LIKE '1' AND customername ILIKE %s 
            ORDER BY customername ASC;
        """
        search_pattern = f"%{cusname}%"
        cursor.execute(sqlstr, (search_pattern,))
        customers  = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print( "Query Operation Error")
    

    return render_template("searchcontact.html" , rows=customers  )



# ************************************************************


@app.route('/showcontactnotes/listcontactnotes/<int:cid>', methods=['GET', 'POST']   )
def listcontactnotes( cid ):    

    customers = []
    try:
        conn = dbconn()
        cursor = conn.cursor()
        sqlstr = """
            SELECT customername, address, phone 
            FROM customer 
            WHERE status LIKE '1' and cid = %s ;
             
        """
        #search_pattern = f"{cusid}"
        cursor.execute(sqlstr, ( cid ,))
        customers  = cursor.fetchall()



        notesqlstr = """
            SELECT contactdetail, submitdate , submittime 
            FROM contact
            WHERE status LIKE '1' and cid = %s ;
             
        """
        #search_pattern = f"{cusid}"
        cursor.execute(notesqlstr, ( cid ,))
        noteslist  = cursor.fetchall()

     

        cursor.close()
        conn.close()
    except Exception as e:
        print( f"Query Operation Error :  {e}" )

    return render_template("showcontactnotes.html" ,   notes=noteslist ,  rows = customers )







# ************************************************************

if __name__ == '__main__':
    # เพิ่ม debug=True จะช่วยให้เห็น Log ได้ชัดขึ้น
    app.run(host='0.0.0.0', port=5000, debug=True)