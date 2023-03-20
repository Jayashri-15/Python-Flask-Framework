from flask import Flask,render_template,request as r,redirect
import pymysql as py

app = Flask('__name__') # s1=student()


@app.route('/')
def index():
    #return 'Hello from index'
    try:
        db = py.connect(host='localhost',user='root',password='Jayashri@15',database='it')
        cur=db.cursor()
        #query="select * from task where is_deleted='N'"  
        query='select * from task'  # all record
        cur.execute(query)
        data=cur.fetchall()
        return render_template('dashboard.html',d=data)
    
    except Exception as e:
        print('Error:',e)
    
    

@app.route('/create')
def create():
    return render_template('form.html')

# Insert
@app.route('/store',methods=['POST'])
def store():
    
    rn = r.form['roll']
    name = r.form['na']
    sub = r.form['sub']
    mark= r.form['mark']
    sta= r.form['sts']
    
    try:
        db = py.connect(host='localhost',user='root',password='Jayashri@15',database='it')
        cur=db.cursor()
        query="insert into task(Roll_No,Name,Subject,Mark,Status)values('{}','{}','{}','{}','{}')".format(rn,name,sub,mark,sta)
        cur.execute(query)
        db.commit()
        return redirect('/')
        
    except Exception as e:
        print('Error:',e)
    


# Delete 
@app.route('/delete/<rid>')
def delete(rid):
    try:
        db = py.connect(host='localhost',user='root',password='Jayashri@15',database='it')
        cur=db.cursor()
        query="delete from task where id='{}'".format(rid) # single record
        #query = "update task SET is_deleted='Y' where id='{}'".format(rid)
        cur.execute(query)
        db.commit()
        return redirect('/')
    
    except Exception as e:
        print('Error:',e)
    
# Edit
@app.route('/edit/<rid>')
def edit(rid):

    try:

        db = py.connect(host='localhost',user='root',password='Jayashri@15',database='it')
        cur=db.cursor()
        query="select * from task where id='{}'".format(rid) # single record
        cur.execute(query)
        data=cur.fetchone()
        return render_template('editform.html',d=data)
    
    except Exception as e:
        print('Error:',e)
    
# Update
@app.route('/update/<rid>',methods=['POST'])

def update(rid):

    urn = r.form['roll']
    uname = r.form['na']
    usub = r.form['sub']
    umark= r.form['mark']
    usta= r.form['sts']

    try:

        db=py.connect(host="localhost",user="root",password="Jayashri@15",database="it")
        cu=db.cursor()
        query="update task SET Roll_No='{}',Name='{}',Subject='{}',Mark='{}',Status='{}' where id='{}'".format(urn,uname,usub,umark,usta,rid)
        cu.execute(query)
        db.commit()
        return redirect('/')

    except Exception as e:
        print("Error:",e)
    
  
    

# run server
app.run(debug=True)  # app==> object and run()==>method of Flask class.

'''
GET Method:
-----------
If form is submitted with GET method then Data submitted by form 
can be seen in the url in the form of key and value.
				 
POST method:
------------
If form is submitted with POST method then Data submitted by form 
cannot be seen in the url in the form of key and value, it send in secured form
(encrypted format).
'''
