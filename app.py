#a lot of this code is based on the course Flask Starter App walkthrough
#https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
#import database.db_connector as db
import os




#********************Configuration********************

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_pierreh'
app.config['MYSQL_PASSWORD'] = '6818' #last 4 of onid
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

    if request.method == "POST":
        if request.form.get("Add_Customer"):

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
            customerValues = (fName,lName,userName,password,birthDate,streetAddress,city,state,zip,telephone,cardNum,securityCode)
            cur = mysql.connection.cursor()
            cur.execute(query, customerValues)
            mysql.connection.commit()
        return redirect('/customers')

    if request.method == "GET":
        query = "SELECT * FROM Customers;"

        cur = mysql.connection.cursor()
        cur.execute(query)
        results = cur.fetchall()
    
        return render_template("customers.j2", customers=results)
    
#*****DELETE*****
@app.route("/delete_customer/<int:id>")
def delete_customer(id):
    query = "DELETE FROM Customers WHERE customerID = '%s'"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/customers")

#*****EDIT*****
@app.route("/edit_customer/<int:id>", methods=["POST","GET"])
def edit_customer(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Customers WHERE customerID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("edit_customer.j2", customer=data)

            # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("edit_customer"):
            # grab user form inputs
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

            # no null inputs
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
            
            customerValues = (fName,lName,userName,password,birthDate,streetAddress,city,state,zip,telephone,cardNum,securityCode,customerID)
            cur = mysql.connection.cursor()
            cur.execute(query, (customerValues))
            mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/customers")    

#**********PRODUCTS**********
#*****CREATE/READ*****
@app.route('/products', methods=["POST","GET"])
def product():

    if request.method == "POST":
        if request.form.get("Add_Product"):

            title = request.form["title"]
            description = request.form["description"]
            retailPrice = request.form["retailPrice"]
            vineyardID = request.form["vineyardID"]


            query = "INSERT INTO Products (title, description, retailPrice, vineyardID) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (title, description, retailPrice, vineyardID))
            mysql.connection.commit()
        return redirect('/products')

    if request.method == "GET":
        query = "SELECT * FROM Products;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        
        query2 = "SELECT * FROM Vineyards;"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        data2 = cur.fetchall()
        
        return render_template("products.j2", products=data, vineyards=data2)
    

#*****DELETE*****
@app.route("/delete_product/<int:id>")
def delete_product(id):
    query = "DELETE FROM Products WHERE productID = '%s'"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/products")

#*****EDIT*****
@app.route("/edit_product/<int:id>", methods=["POST","GET"])
def edit_product(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Products WHERE productID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT * FROM Vineyards"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        data2 = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("edit_product.j2", product=data, vineyards=data2)

            # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("edit_product"):
            # grab user form inputs
            productID = request.form["productID"]
            title = request.form["title"]
            description = request.form["description"]
            retailPrice = request.form["retailPrice"]
            vineyardID = request.form["vineyardID"]

            query = "UPDATE Products SET title =%s, description =%s, retailPrice = %s,vineyardID = %s WHERE productID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (title, description, retailPrice, vineyardID, productID))
            mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/products")    
        
#**********VINEYARDS**********
#*****CREATE/READ*****
@app.route('/vineyards', methods=["POST","GET"])
def vineyard():

    if request.method == "POST":
        if request.form.get("Add_vineyard"):

            title = request.form["title"]
            description = request.form["description"]
            casesYearly = request.form["casesYearly"]
            yearFounded = request.form["yearFounded"]
            website = request.form["website"]
            
            query = "INSERT INTO Vineyards (title, description, casesYearly, yearFounded, website) VALUES (%s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (title, description, casesYearly, yearFounded, website))
            mysql.connection.commit()

            return redirect('/vineyards')

    if request.method == "GET":
        query = "SELECT * FROM Vineyards;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()
        
        return render_template("vineyards.j2", vineyards=data)
    
#*****DELETE*****
@app.route("/delete_vineyard/<int:id>")
def delete_vineyard(id):
    query = "DELETE FROM Vineyards WHERE vineyardID = '%s'"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/vineyards")        

#*****EDIT*****
@app.route("/edit_vineyard/<int:id>", methods=["POST","GET"])
def edit_vineyard(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Vineyards WHERE vineyardID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("edit_vineyard.j2", vineyard=data)

            # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("edit_vineyard"):
            # grab user form inputs
            vineyardID = request.form["vineyardID"]
            title = request.form["title"]
            description = request.form["description"]
            casesYearly = request.form["casesYearly"]
            yearFounded = request.form["yearFounded"]
            website = request.form["website"]

            
            query = "UPDATE Vineyards SET title =%s, description =%s, casesYearly = %s,yearFounded = %s,website = %s WHERE vineyardID = %s"
            cur = mysql.connection.cursor()
            cur.execute(query, (title, description, casesYearly, yearFounded, website, vineyardID))
            mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/vineyards")    

#**********ORDERS**********
#*****CREATE/READ*****
@app.route('/orders', methods=["POST","GET"])
def Orders():

    if request.method == "POST":
        if request.form.get("Add_Order"):

            datePurchased = request.form["datePurchased"]
            customerID = request.form["customerID"]
            
            query = "INSERT INTO Orders (datePurchased, customerID) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (datePurchased, customerID))
            mysql.connection.commit()

            return redirect('/orders')
        
        if request.form.get("Add_Product_Order"):

            orderID = request.form["orderID"]
            productID = request.form["productID"]
            quantity = request.form["quantity"]
            
            query = "INSERT INTO OrderProducts (orderID, productID, quantity) VALUES (%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (orderID, productID, quantity))
            mysql.connection.commit()

            return redirect('/orders')
        
    if request.method == "GET":
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
        
        query2 = "SELECT * FROM Customers"

        cur = mysql.connection.cursor()
        cur.execute(query2)
        results2 = cur.fetchall()

        query3 = "SELECT * FROM Products"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        results3 = cur.fetchall()

        query4 = "SELECT * FROM Orders"
        cur = mysql.connection.cursor()
        cur.execute(query4)
        results4 = cur.fetchall()

        return render_template("orders.j2", orders=results1, customers=results2, products=results3, bulkorders=results4)

#*****DELETE*****
@app.route("/delete_order/<int:id>")
def delete_order(id):
    query = "DELETE FROM Orders WHERE orderID = '%s'"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    return redirect("/orders")        

@app.route("/delete_order_item/<int:id1>/<int:id2>")
def delete_order_item(id1, id2):
    query = "DELETE FROM OrderProducts WHERE orderID = %s AND productID = %s"
    cur = mysql.connection.cursor()
    cur.execute(query, (id1, id2))
    mysql.connection.commit()

    return redirect("/orders")     

#*****EDIT*****
@app.route("/edit_order/<int:id>", methods=["POST","GET"])
def edit_order(id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Orders WHERE orderID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query1 = "SELECT * FROM OrderProducts WHERE orderID = %s" % (id)
        cur = mysql.connection.cursor()
        cur.execute(query1)
        data1 = cur.fetchall()

        query2 = "SELECT * FROM Products"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        data2 = cur.fetchall()

        query3 = "SELECT customerID FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        data3 = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("edit_order.j2", order=data, orderproducts=data1, products=data2, customers=data3)

            # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button
        if request.form.get("edit_order"):
            # grab user form inputs
            orderID = request.form["orderID"]
            customerID = request.form["customerID"]
            datePurchased = request.form["datePurchased"]
            productID = request.form["productID"]
            quantity = request.form["quantity"]


            query = "UPDATE OrderProducts SET productID = %s, quantity = %s WHERE orderID = %s AND productID = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query, (productID, quantity, orderID, productID))
            mysql.connection.commit()

            query1 = "UPDATE Orders SET datePurchased = %s, customerID = %s WHERE orderID = %s AND customerID = %s;"
            cur = mysql.connection.cursor()
            cur.execute(query1, (datePurchased, customerID, orderID, customerID))
            mysql.connection.commit()

            # redirect back to people page after we execute the update query
            return redirect("/orders")    

# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=15472, debug=True)