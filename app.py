from flask import Flask, render_template, request, redirect , url_for
import psycopg2  
from app.connectdb import dbconn

from app.createtable_contact import createtable_contact
from app.createtable_customer import createtable_customer
from app.insertdata_customer import insertdata_customer
from app.insertdata_contact import insertdata_contact


from datetime import datetime

app = Flask(__name__)
 
 
 

# ************************************************************


@app.route("/createtableschema")
def createdataschema():

    word = []
    word.append('Start')

    ####
    try:
        createtable_customer()
        word.append ("Create Table Customer Success"  )  
    except:
        word.append ( "Table Customer  Failed")

    ####
    try:
        createtable_contact()
        word.append  ("Create Table Contact Success")
    except:
        word.append   ("Table Contact Failed")

    ####
    try:
        insertdata_customer()
        word.append ( "Insert Data Customer Success" )   
    
    except:
        word.append ( "Table customer Failed")


    ####
    try:
        insertdata_contact()
        word.append ( "Insert Data Contact Success" ) 
    except:
        word.append ( "Insert Contact  Failed")

    return render_template("back.html"  , show=word )




@app.route("/xxxx")
def custom():
        return "Hello"






































 



@app.route("/")
def selectdata():
    customers = []
    try:
        conn = dbconn()
        cursor = conn.cursor()
        cursor.execute("SELECT cid, customername, taxid, address , phone FROM customer  where status like '1'  order by cid asc;")
        customers  = cursor.fetchall()
 
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
def insertcustomer():
    if request.method == 'POST':
  

        customername = request.form.get('customername')
        taxid = request.form.get('taxid')
        address = request.form.get('address')        
        phone = request.form.get('phone')
 
        conn = dbconn()
        cursor = conn.cursor()
        
        sql_query = "INSERT INTO customer ( customername,taxid,address,phone,status) VALUES (%s, %s, %s, %s ,%s) ; "
 
        cursor.execute(sql_query, (customername,taxid,address,phone,'1'))
        
        conn.commit()   
        cursor.close()  
        conn.close()    
        
 
    return redirect('/')

# ************************************************************





# ************************************************************

@app.route("/customers")
def listcompany():
    customers = []
    try:
        conn = dbconn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer where status like '1'  ;")
        customers  = cursor.fetchall()
 
        print("DEBUG: ข้อมูลที่ได้จาก DB คือ:", customers)
   
        cursor.close()
        conn.close()
    except Exception as e:
        print( "Query Operation Error")

    return render_template("listcompany.html"  , rows=customers)
 
# ************************************************************



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



# ************************************************************

@app.route('/customers/update/<int:cid>', methods=['GET', 'POST']  )
def updatecompany( cid ):

 
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
        
 
    conn = dbconn()
    cursor = conn.cursor()


    cursor.execute(sql_query, ( customername , taxid , address , phone ,cusid))
    conn.commit()
 
    return redirect('/')

# ************************************************************
 


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



# ************************************************************

@app.route('/customers/deleteconfirm/<int:cid>', methods=['GET', 'POST']  )
def deletecuctomerconfirm( cid ):

 
    cusid = str(cid)
 
    sql_query = """
            UPDATE customer 
            SET status = %s
            WHERE cid = %s
        """
        
 
    conn = dbconn()
    cursor = conn.cursor()
    cursor.execute(sql_query, ( '0' , cusid))
    conn.commit()
 
 
    return redirect('/')

# ************************************************************



# ************************************************************

@app.route('/contactnotes')
def addnewcontactform():    
    customers = []
    try:
        conn = dbconn()
        cursor = conn.cursor()
        cursor.execute("SELECT cid , customername  FROM customer where status like '1' order by customername asc ;")
        customers  = cursor.fetchall()
 
        print("DEBUG: ข้อมูลที่ได้จาก DB คือ:", customers)
        # ---------------------------------
        cursor.close()
        conn.close()
    except Exception as e:
        print( "Query Operation Error")

    return render_template("addnewcontactform.html"  , rows=customers)


# ************************************************************



# ************************************************************

@app.route('/contactnotes/addnewcontact'  , methods=['GET', 'POST']  )
def addnewcontact():    

    if request.method == 'POST':
 
        cid = request.form.get('cid')
        contactdetail = request.form.get('contactnotes')

        dotimenow = datetime.now()
        do_date = dotimenow.strftime("%d/%m/%Y")
        do_time = dotimenow.strftime("%H:%M:%S")

        status = "1" 
 
        conn = dbconn()
        cursor = conn.cursor()
        
        sql_query = "INSERT INTO contact ( contactdetail,cid,status , submitdate ,submittime) VALUES (%s, %s, %s, %s, %s) ; "
    
 
        cursor.execute(sql_query, ( contactdetail , cid , status , do_date, do_time ))
        
        conn.commit()  
        cursor.close()  
        conn.close()    
        
 
    return redirect('/')

# ************************************************************



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
 
        cursor.execute(sqlstr, ( cid ,))
        customers  = cursor.fetchall()



        notesqlstr = """
            SELECT contactdetail, submitdate , submittime 
            FROM contact
            WHERE status LIKE '1' and cid = %s ;
             
        """
 
        cursor.execute(notesqlstr, ( cid ,))
        noteslist  = cursor.fetchall()

     

        cursor.close()
        conn.close()
    except Exception as e:
        print( f"Query Operation Error :  {e}" )

    return render_template("showcontactnotes.html" ,   notes=noteslist ,  rows = customers )


# ************************************************************




# ************************************************************

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=True)