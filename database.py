import mysql.connector


def ConnectorMysql():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="check_cadet",
        # auth_plugin='mysql_native_password'
    )
    
    # print('successful')
    return mydb

ConnectorMysql()


# def get_data(nogun):
#     mydb = ConnectorMysql()
#     mycursor = mydb.cursor()
#     sql = ("SELECT * FROM gun WHERE nogun='{}';".format(nogun))
#     mycursor.execute(sql)
#     myresult = mycursor.fetchall()

#     for x in myresult:
#         arr = {
#             "nogun": x[0],
#             "uname": x[1],
#             "pickup": int(x[2]),
#             "broken": x[3],
#             "lost": x[3],
#             "remaining": x[3]
#         }
#     return arr

# Done
def get_alldata():
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("SELECT * FROM cadet")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    print(myresult)
    return myresult
get_alldata()



def inbatt(uname):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = ("UPDATE cadet SET stay = 1, out = 0 WHERE uname = %s;")
    val =(uname)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()
    

# # SUM PICKUP
# def get_pickup():
#     mydb = ConnectorMysql()
#     mycursor = mydb.cursor()
#     sql = ("SELECT SUM(pickup)FROM gun;")
#     mycursor.execute(sql)
#     myresult = mycursor.fetchall()

#     for x in myresult:

#         print(x)
#     return x

# # SUM LOST


# def get_lost():
#     mydb = ConnectorMysql()
#     mycursor = mydb.cursor()
#     sql = ("SELECT SUM(lost)FROM gun;")
#     mycursor.execute(sql)
#     myresult = mycursor.fetchall()

#     for x in myresult:
#         print(x)
#     return x

# # SUM BROKEN


# def get_broken():
#     mydb = ConnectorMysql()
#     mycursor = mydb.cursor()
#     sql = ("SELECT SUM(broken)FROM gun;")
#     mycursor.execute(sql)
#     myresult = mycursor.fetchall()

#     for x in myresult:
#         print(x)
#     return x

# # SUM REMAINING


# def get_remaining():
#     mydb = ConnectorMysql()
#     mycursor = mydb.cursor()
#     sql = ("SELECT SUM(remaining)FROM gun;")
#     mycursor.execute(sql)
#     myresult = mycursor.fetchall()

#     for x in myresult:
#         print(x)
#     return x

# input
# localhost:5000/insert?uname=C&pickup=0&broken=1&lost=0&remaining=0&nogun=3


def insert_data(id, uname, lname, stay, out):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    # sql = "INSERT INTO cadet (id, uname, lname, stay, out) VALUES (%s ,%s, %s, %s, %s)"
    sql = "INSERT INTO cadet (id, uname, lname, stay, out) VALUES (2 ,, %s, %s, %s)"
    val = (id, uname, lname, stay, out)
    mycursor.execute(sql, val)
    print('success')
    mydb.commit()
    mycursor.close()
    mydb.close()



    
    


# # localhost:5000/update?pickup=0&broken=1&lost=0&remaining=0&nogun=1
# def update_data(pickup, broken, lost, remaining, nogun):
#     mydb = ConnectorMysql()
#     mycursor = mydb.cursor()
#     sql = "UPDATE gun SET pickup=%s , broken=%s , lost=%s , remaining=%s  WHERE nogun=%s"
#     val = (pickup, broken, lost, remaining, nogun)
#     mycursor.execute(sql, val)
#     mydb.commit()
#     mycursor.close()
#     mydb.close()

# # localhost:5000/delete?nogun=3


# def delete_data(nogun):
#     mydb = ConnectorMysql()
#     mycursor = mydb.cursor()
#     sql = "DELETE  FROM gun WHERE nogun={}".format(nogun)
#     mycursor.execute(sql)
#     mydb.commit()
#     mycursor.close()
#     mydb.close()
