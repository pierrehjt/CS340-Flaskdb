#written by: Henri Pierre and David Tuney
#a lot of this code is based on the course Flask Starter App walkthrough
#https://github.com/osu-cs340-ecampus/flask-starter-app
#lastEdited:03/20/2023*/

from flask import Flask, render_template, redirect
from flask_mysqldb import MySQL
from flask import request
import os




#********************Configuration********************
#this mysql connection code based off the starter app
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_pierreh'
app.config['MYSQL_PASSWORD'] = '6818' 
app.config['MYSQL_DB'] = 'cs340_pierreh'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)



#********************Routes********************

#INDEX
@app.route('/')
def root():

    return redirect('/customers')

#**********CUSTOMERS**********
#*****CREATE/READ*****
@app.route('/customers', methods=["POST","GET"])
def customer():

    #if form is submitted
    if request.method == "POST":
        if request.form.get("Add_Customer"):

            #get all data from form
            userName = request.form["userName"]
            password = request.form["password"]
            fName = request.form["fName"]
            lName = request.form["lName"]
            birthDate = request.form["birthDate"]
            telephone = request.form["telephone"]
            streetAddress = request.form["streetAddress"]
            city = request.form["city"]
            state = request.form["state"]
            zip = request.form["zip"]
            cardNum = request.form["cardNum"]
            securityCode = request.form["securityCode"]

            #values acquired from form
            customerValues = (fName,lName,userName,password,birthDate,streetAddress,city,state,zip,telephone,cardNum,securityCode)

            # query with placeholder values
            query = "INSERT INTO Customers (\
                        fName,\
                        lName,\
                        userName,\
                        password,\
                        birthDate,\
                        streetAddress,\
                        city,\
                        state,\
                        zip,\
                        telephone,\
                        cardNum,\
                        securityCode\
                    )\
                    Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            #execute query with values acquired from form
            cur = mysql.connection.cursor()
            cur.execute(query, customerValues)
            mysql.connection.commit()

        #return to page
        return redirect('/customers')

    #if page is accessed
    if request.method == "GET":

        #select all data to display
        query = "SELECT * FROM Customers;"

        #run query to read data
        cur = mysql.connection.cursor()
        cur.execute(query)
        results = cur.fetchall()

        #render page with returned data
        return render_template("customers.j2", customers=results)
    
#*****DELETE*****
@app.route("/delete_customer/<int:id>")
def delete_customer(id):
    #create query to delete customer specified by user input
    query = "DELETE FROM Customers WHERE customerID = '%s'"

    #execute delete query
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    #redirect to initial page
    return redirect("/customers")

#*****EDIT*****
@app.route("/edit_customer/<int:id>", methods=["POST","GET"])
def edit_customer(id):

    #if edit form is requested
    if request.method == "GET":
        
        #get all data on specific customer
        query = "SELECT * FROM Customers WHERE customerID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        #render edit page with specified ID data
        return render_template("edit_customer.j2", customer=data)

    #if edit form is submitted
    if request.method == "POST":
        if request.form.get("edit_customer"):
            
            #get all data from form
            customerID = request.form["customerID"]
            userName = request.form["userName"]
            password = request.form["password"]
            fName = request.form["fName"]
            lName = request.form["lName"]
            birthDate = request.form["birthDate"]
            telephone = request.form["telephone"]
            streetAddress = request.form["streetAddress"]
            city = request.form["city"]
            state = request.form["state"]
            zip = request.form["zip"]
            cardNum = request.form["cardNum"]
            securityCode = request.form["securityCode"]

            #values acquired from form
            customerValues = (fName,lName,userName,password,birthDate,streetAddress,city,state,zip,telephone,cardNum,securityCode,customerID)

            # query with placeholder values
            query = "UPDATE Customers SET \
                        fName = %s,\
                        lName = %s,\
                        userName = %s,\
                        password = %s,\
                        birthDate = %s,\
                        streetAddress = %s,\
                        city = %s,\
                        state = %s,\
                        zip = %s,\
                        telephone = %s,\
                        cardNum = %s,\
                        securityCode = %s\
                    WHERE customerID = %s"
            
            #execute query with values acquired from form
            cur = mysql.connection.cursor()
            cur.execute(query, (customerValues))
            mysql.connection.commit()

            #return to customers page
            return redirect("/customers")    

#**********PRODUCTS**********
#*****CREATE/READ*****
@app.route('/products', methods=["POST","GET"])
def product():

    #if form is submitted
    if request.method == "POST":
        if request.form.get("Add_Product"):

            #get all data from form
            title = request.form["title"]
            description = request.form["description"]
            retailPrice = request.form["retailPrice"]
            vineyardID = request.form["vineyardID"]

            #values acquired from form
            productValues = (title, description, retailPrice, vineyardID)

            # query with placeholder values
            query = "INSERT INTO Products (title, description, retailPrice, vineyardID) VALUES (%s, %s, %s, %s)"

            #execute query with values acquired from form
            cur = mysql.connection.cursor()
            cur.execute(query, productValues)
            mysql.connection.commit()

        #return to page
        return redirect('/products')


    #if page is accessed
    if request.method == "GET":

        #select all data to display
        query = "SELECT * FROM Products;"
          
        #run query to read data
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        #select vineyard data for dropdown
        query2 = "SELECT * FROM Vineyards;"

        #run query to read data
        cur = mysql.connection.cursor()
        cur.execute(query2)
        data2 = cur.fetchall()
        
        #render page with returned data
        return render_template("products.j2", products=data, vineyards=data2)
    

#*****DELETE*****
@app.route("/delete_product/<int:id>")
def delete_product(id):

    #create query to delete product specified by user input
    query = "DELETE FROM Products WHERE productID = '%s'"

    #execute delete query
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    #redirect to initial page
    return redirect("/products")

#*****EDIT*****
@app.route("/edit_product/<int:id>", methods=["POST","GET"])
def edit_product(id):

    #if edit form is requested
    if request.method == "GET":
       

        #get all data on specific prdouct
        query = "SELECT * FROM Products WHERE productID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        #select vineyard data for dropdown
        query2 = "SELECT * FROM Vineyards"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        data2 = cur.fetchall()

        #render edit page with specified ID data and vineyard data
        return render_template("edit_product.j2", product=data, vineyards=data2)

    #if edit form is submitted
    if request.method == "POST":
        if request.form.get("edit_product"):

            #get all data from form
            productID = request.form["productID"]
            title = request.form["title"]
            description = request.form["description"]
            retailPrice = request.form["retailPrice"]
            vineyardID = request.form["vineyardID"]

            #values acquired from form
            productValues = (title, description, retailPrice, vineyardID, productID)

            # query with placeholder values
            query = "UPDATE Products SET title =%s, description =%s, retailPrice = %s,vineyardID = %s WHERE productID = %s"

            #execute query with values acquired from form
            cur = mysql.connection.cursor()
            cur.execute(query, productValues)
            mysql.connection.commit()

            #return to products page
            return redirect("/products")    
        
#**********VINEYARDS**********
#*****CREATE/READ*****
@app.route('/vineyards', methods=["POST","GET"])
def vineyard():

    #if form is submitted
    if request.method == "POST":
        if request.form.get("Add_vineyard"):

            #get all data from form
            title = request.form["title"]
            description = request.form["description"]
            casesYearly = request.form["casesYearly"]
            yearFounded = request.form["yearFounded"]
            website = request.form["website"] 

            #values acquired from form
            vineyardValues = (title, description, casesYearly, yearFounded, website)
            
            # query with placeholder values
            query = "INSERT INTO Vineyards (title, description, casesYearly, yearFounded, website) VALUES (%s, %s, %s, %s, %s)"

            #execute query with values acquired from form
            cur = mysql.connection.cursor()
            cur.execute(query, vineyardValues)
            mysql.connection.commit()

            #return to page
            return redirect('/vineyards')

    #if page is accessed
    if request.method == "GET":

        #select all data to display
        query = "SELECT * FROM Vineyards;"

        #run query to read data
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        
        #render page with returned data
        return render_template("vineyards.j2", vineyards=data)
    
#*****DELETE*****
@app.route("/delete_vineyard/<int:id>")
def delete_vineyard(id):

    #create query to delete customer specified by user input
    query = "DELETE FROM Vineyards WHERE vineyardID = '%s'"

    #execute delete query
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    #redirect to initial page
    return redirect("/vineyards")        

#*****EDIT*****
@app.route("/edit_vineyard/<int:id>", methods=["POST","GET"])
def edit_vineyard(id):

    #if edit form is requested
    if request.method == "GET":

        #get all data on specific vineyard
        query = "SELECT * FROM Vineyards WHERE vineyardID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        #render edit page with specified ID data
        return render_template("edit_vineyard.j2", vineyard=data)

    #if edit form is submitted
    if request.method == "POST":
        if request.form.get("edit_vineyard"):

            #get all data from form
            vineyardID = request.form["vineyardID"]
            title = request.form["title"]
            description = request.form["description"]
            casesYearly = request.form["casesYearly"]
            yearFounded = request.form["yearFounded"]
            website = request.form["website"]

            #values acquired from form
            vineyardValues = (title, description, casesYearly, yearFounded, website, vineyardID)

            # query with placeholder values
            query = "UPDATE Vineyards SET title =%s, description =%s, casesYearly = %s,yearFounded = %s,website = %s WHERE vineyardID = %s"
            
            cur = mysql.connection.cursor()
            cur.execute(query, vineyardValues)
            mysql.connection.commit()

            #return to vineyards page
            return redirect("/vineyards")    

#**********ORDERS**********
#*****CREATE/READ*****
@app.route('/orders', methods=["POST","GET"])
def Orders():

    #if form is submitted
    if request.method == "POST":
        #if form is to add an order
        if request.form.get("Add_Order"):

            #get all data from form
            datePurchased = request.form["datePurchased"]
            customerID = request.form["customerID"]

            # query with placeholder values
            query = "INSERT INTO Orders (datePurchased, customerID) VALUES (%s, %s)"

            #values acquired from form
            orderValues = (datePurchased, customerID)

            #execute query with values acquired from form
            cur = mysql.connection.cursor()
            cur.execute(query, orderValues)
            mysql.connection.commit()

            #return to page
            return redirect('/orders')
        
        #if form is to add product(s) to an order
        if request.form.get("Add_Product_Order"):

            #get all data from form
            orderID = request.form["orderID"]
            productID = request.form["productID"]
            quantity = request.form["quantity"]

            #check to see if selected product is already assosciated with order
            
            #find product id in order
            query0 = "SELECT productID FROM OrderProducts WHERE orderID = %s AND productID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query0, (orderID, productID))
            data0 = cur.fetchone()
            #find product id in products
            query1 = "SELECT productID FROM Products WHERE productID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query1, (productID))
            data1 = cur.fetchone()

            #if product doesn't exist in current order, add to order
            if data0 != data1:
                # query with placeholder values
                query2 = "INSERT INTO OrderProducts (orderID, productID, quantity) VALUES (%s, %s, %s)"

                #execute query with values acquired from form
                cur = mysql.connection.cursor()
                cur.execute(query2, (orderID, productID, quantity))
                mysql.connection.commit()

            #if product already exists in order, add its quantity to existing value and update order
            else:
                query3 = "UPDATE OrderProducts SET quantity = quantity + %s WHERE orderID = %s AND productID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query3, (quantity, orderID, productID))
                mysql.connection.commit()
                return redirect('/orders')
                
            #return to page
            return redirect('/orders')
        
    #if page is accessed
    if request.method == "GET":

        #select all data to display
        query1 = "SELECT \
                    Orders.datePurchased,\
                    Customers.customerID,\
                    Orders.orderID,\
                    Products.productID,\
                    Products.title,\
                    sum(OrderProducts.quantity) as quantity_ordered,\
                    sum(Products.retailPrice * OrderProducts.quantity) as total_price\
                From Customers\
                    JOIN Orders ON Customers.customerID = Orders.customerID\
                    JOIN OrderProducts ON Orders.orderID = OrderProducts.orderID\
                    LEFT JOIN Products ON OrderProducts.productID = Products.productID\
                GROUP BY orderID, Products.productID"
        cur = mysql.connection.cursor()
        cur.execute(query1)
        results1 = cur.fetchall()
        
        #select customers for dropdown
        query2 = "SELECT * FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        results2 = cur.fetchall()

        #select products for dropdown
        query3 = "SELECT * FROM Products"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        results3 = cur.fetchall()

        #select orders for dropdown
        query4 = "SELECT * FROM Orders"
        cur = mysql.connection.cursor()
        cur.execute(query4)
        results4 = cur.fetchall()

        #render page with returned data
        return render_template("orders.j2", orders=results1, customers=results2, products=results3, bulkorders=results4)

#*****DELETE*****
#delete entire order
@app.route("/delete_order/<int:id>")
def delete_order(id):

    #create query to delete order specified by user input
    query = "DELETE FROM Orders WHERE orderID = '%s'"

    #execute delete query
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    #redirect to initial page
    return redirect("/orders")        

#delete product(s) from an order
@app.route("/delete_order_item/<int:id1>/<int:id2>")
def delete_order_item(id1, id2):
    #create query to delete product from order specified by user input
    query = "DELETE FROM OrderProducts WHERE orderID = %s AND productID = %s"

    #execute delete query
    cur = mysql.connection.cursor()
    cur.execute(query, (id1, id2))
    mysql.connection.commit()

    #redirect to initial page
    return redirect("/orders")     

#*****EDIT*****
@app.route("/edit_order/<int:id>/<int:id2>", methods=["POST","GET"])
def edit_order(id, id2):

    #if edit form is requested
    if request.method == "GET":

        #get all data on specific order
        query = "SELECT * FROM Orders WHERE orderID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        #get all data on specific orderproduct for order
        query1 = "SELECT * FROM OrderProducts WHERE orderID = %s AND productID = %s" % (id, id2)
        cur = mysql.connection.cursor()
        cur.execute(query1)
        data1 = cur.fetchall()

        #get all products for dropdown
        query2 = "SELECT * FROM Products"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        data2 = cur.fetchall()

        #render edit page with specified data
        return render_template("edit_order.j2", order=data, orderproducts=data1, products=data2)

    #if edit form is submitted
    if request.method == "POST":
        if request.form.get("edit_order"):

            #get all data from form
            orderID = request.form["orderID"]
            customerID = request.form["customerID"]
            oldproductID = request.form["oldproductID"]
            datePurchased = request.form["datePurchased"]
            productID = request.form["productID"]
            quantity = request.form["quantity"]

            #values acquired from form
            #OrderProducts
            orderProductValues = (productID, quantity, orderID, oldproductID)
            #Orders
            orderValues = (datePurchased, orderID, customerID)

            #find product id in order
            query0 = "SELECT productID FROM OrderProducts WHERE orderID = %s AND productID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query0, (orderID, productID))
            data0 = cur.fetchone()
            #find product id in products
            query1 = "SELECT productID FROM Products WHERE productID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query1, (productID))
            data1 = cur.fetchone()

            #if product doesn't exist in current order, add to order
            if data0 != data1:
                # query with placeholder values
                query2 = "UPDATE OrderProducts SET productID = %s, quantity = %s WHERE orderID = %s AND productID = %s;"

                #execute query with values acquired from form
                cur = mysql.connection.cursor()
                cur.execute(query2, orderProductValues)
                mysql.connection.commit()

            #if productID hasn't changed, only update quantity
            elif oldproductID == productID:

                query3 ="UPDATE OrderProducts SET productID = %s, quantity = %s WHERE orderID = %s AND productID = %s;"
                #execute query with values acquired from form
                cur = mysql.connection.cursor()
                cur.execute(query3, (oldproductID, quantity, orderID, oldproductID))
                mysql.connection.commit()

            #if product already exists in order, add its quantity to existing value, update order, delete previous order
            else:
                
                query4 = "UPDATE OrderProducts SET quantity = quantity + %s WHERE orderID = %s AND productID = %s;"
                cur = mysql.connection.cursor()
                cur.execute(query4, (quantity, orderID, productID))
                mysql.connection.commit()

                query5 = "DELETE FROM OrderProducts WHERE orderID = %s AND productID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query5, (orderID, oldproductID))
                mysql.connection.commit()

            #now update Orders
            # query with placeholder values
            query6 = "UPDATE Orders SET datePurchased = %s WHERE orderID = %s AND customerID = %s;"

            #execute query with values acquired from form
            cur = mysql.connection.cursor()
            cur.execute(query6, orderValues)
            mysql.connection.commit()

            #return to orders page
            return redirect("/orders")    


# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=15472, debug=True)