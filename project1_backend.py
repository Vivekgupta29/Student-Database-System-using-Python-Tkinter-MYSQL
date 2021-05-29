import mysql.connector
#import project1_frontend

def studentData():
        con = mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="project2")
        cur=con.cursor()
       
        cur.execute("CREATE TABLE student (stdid int primary key,namestudent text,rollno int(10),dob text,gender text,address text,mobile int(10))")
        con.commit()
        con.close()     

def addStdRec(stdid,name,rollno,dob,gender,address,mobile):
        con = mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="project2")
        cur=con.cursor()
        cur.execute("use project2")
        cur.execute("INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s)",(stdid,name,rollno,dob,gender,address,mobile))
        con.commit()
        con.close() 

def viewData():
        con = mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="project2")
        cur=con.cursor()
        cur.execute("use project2")
        cur.execute("select stdid,name,rollno,dob,gender,address,mobile from student order by stdid")
        row=cur.fetchall()
        con.close()       
        return row

def deleteRec(stdid):
        con = mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="project2")
        cur=con.cursor()
        cur.execute("use project2")
        given_std=stdid

        sql = "DELETE FROM student WHERE stdid='%s'" % (given_std)
        cur.execute(sql)
        con.commit()
        con.close()     

def searchData(stdid="",name="",rollno="",dob="",gender="",address="",mobile=""):
        con = mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="project2")
        cur=con.cursor()
        cur.execute("use project2")
        
        select_query="SELECT stdid,name,rollno,dob,gender,address,mobile FROM student where stdid=%s or name=%s or rollno=%s or dob=%s or gender=%s or address=%s or mobile=%s"
        std=(stdid,name,rollno,dob,gender,address,mobile)
        cur.execute(select_query,std,)
        rows=cur.fetchall()
        con.close()        
        return rows
        
def dataUpdate(stdid="",name="",rollno="",dob="",gender="",address="",mobile=""):
        con = mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="project2")
        cur=con.cursor()
        cur.execute("use project2")
        cur.execute("UPDATE student SET stdid=%s,name=%s,rollno=%s,dob=%s,age=%s,gender=%s,address=%s,mobile=%s WHERE id=%s",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close()    
