from flask import Flask, render_template,request,flash
import time
import random
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='frappe_assess'
mysql = MySQL(app)


@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
   
    if request.method =='POST':
        userDetails = request.form
        name=userDetails['name']
        origin=userDetails['Origin']
        destination =userDetails['destination']
        cur =mysql.connection.cursor()
        cur.execute("select * from product where productname =%s",(name,))
        row_count = cur.rowcount
        if row_count==0:
            if origin=="":
                if destination=="":
                    return render_template('index.html',message='Destination is empty..Try Again')
                else:
                    proid = random.randint(4,100)
                    movid=random.randint(4,100)
                    timeStr = time.ctime()
                    print('Current Timestamp : ', timeStr)          
                    cur.execute("INSERT INTO product(productID,productname, location_name) VALUES (%s,%s,%s)",(proid,name,destination,))
                    cur.execute("INSERT INTO movement(movementID,productname,fromlocation,tolocation,timestamp) VALUES (%s,%s,%s,%s,%s)",(movid,name,origin,destination,timeStr,))
                    mysql.connection.commit()
                    cur.close()
                    return render_template('index.html',message='New product added')
            else:
                return render_template('index.html',message='To add a new product, Make sure the origin column is empty')
                
            
            
        else:
                if origin=="":
                    return render_template('index.html',message='Please select the origin location of the product')
                else:
                    if destination=="":
                        timeStr = time.ctime()
                        cur.execute("DELETE FROM prduct WHERE product_name=%s",(name))
                        cur.execute("INSERT INTO movement(movementID,productname,fromlocation,tolocation,timestamp) VALUES (%s,%s,%s,%s,%s)",(movid,name,origin,destination,timeStr,))
                        mysql.connection.commit()
                        return render_template('index.html',message='Product out of the inventory, Record removed..')

                    else:
                        movid=random.randint(4,100)
                        timeStr = time.ctime()
                        cur.execute("UPDATE product SET location_name= %s WHERE productname = %s",(destination,name,))
                        cur.execute("INSERT INTO movement(movementID,productname,fromlocation,tolocation,timestamp) VALUES (%s,%s,%s,%s,%s)",(movid,name,origin,destination,timeStr,))

                        mysql.connection.commit()
                        cur.close()
                    
                return render_template('index.html',message='Product Location updated')


           
            

    return render_template('index.html')


@app.route('/home')
def homepage():
   return render_template('index.html')  
   
@app.route('/products')
def productspage():
        cur =mysql.connection.cursor()
        cur.execute("select * from product");
        rows = cur.fetchall()
        return render_template('product.html',rows=rows) 



@app.route('/inventories')
def inventory():
            cur =mysql.connection.cursor()
            cur.execute("select location_name, count(*) from product Group by location_name order by location_name ASC");
            rows = cur.fetchall()
            return render_template('inventories.html',rows=rows) 




   

@app.route('/shippings')
def reports():
    cur =mysql.connection.cursor()
    cur.execute("select * from movement");
    rows = cur.fetchall()
    return render_template('shippings.html',rows=rows)  

     


if __name__== '__main__':   
    app.run(debug=True)
    


    


 
