class login_menu():
    def __init__(self,user ="sql11479097", password = "rNkd8Ay8H7", host="sql11.freemysqlhosting.net", database = "sql11479097"):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
    
    ### Import mysql connector ###    
    import mysql.connector
    connection = mysql.connector.connect(user ="sql11479097", password = "rNkd8Ay8H7", host="sql11.freemysqlhosting.net", database = "sql11479097")
    
    cursor = connection.cursor()
    ##############################
    
    def get_all_data(self, cursor = cursor):
        """printuje wszystie dane użytkowników"""
        query = f"SELECT * FROM sql11479097.users;"
        cursor.execute(query)

        for line in cursor:
            print(line)
    
    def log_in(self, username, password, cursor = cursor):
        """funkcja zwraca nazwe użytkownika jeśli istnieje"""
        query = f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}';"
        cursor.execute(query)
        #### checking
        for id in cursor:
            if id[0] == None:
                return False
            else:
                return(username)