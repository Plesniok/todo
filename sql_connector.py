import mysql.connector

connection = mysql.connector.connect(user ="sql11479097", password = "rNkd8Ay8H7", host="sql11.freemysqlhosting.net", database = "todov2")

def user_valid(username1, password1):
    import mysql.connector





    cursor = connection.cursor()



    
#insertQuery = "INSERT INTO users2(username, city) VALUES (%(username)s, %(city)s);"
#insert_data = {'username' : 'Mariusz', 'city' : "kato"}
#cursor.execute(insertQuery, insert_data)

    #connection.commit()

    query = f"SELECT id FROM users WHERE username = '{username1}' AND password = '{password1}';"
    cursor.execute(query)

    for id in cursor:
        if id[0] == None:
            return False
        else:
            return(username1)
    
#def user_registration(new_username, new_password):
    #connection.close()
print(user_valid("admin", "admin"))