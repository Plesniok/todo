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
    
    def register(self, new_username, new_password, cursor = cursor):
        """funkcja wprowadza dane użytkownika do bazy danych
        oraz printuje jeśli się udało"""
        insertQuery = "INSERT INTO users(username, password) VALUES (%(username)s, %(password)s);"
        insert_data = {'username' : new_username, 'password' : new_password}
        cursor.execute(insertQuery, insert_data)

        self.connection.commit()
        print(f"witaj: {new_username}!")
    
    ### nie wiem czemu wczesniej cursor
    # w argumencie działał, a w tym przypadku nie działa
    
    def register_valid(self, new_username):
        """funkcja zwraca None, jeśli nie ma duplikatów,
        False jeśli występują"""
        cursor = self.connection.cursor()
        query = f"SELECT username FROM users WHERE username = '{new_username}';"
        cursor.execute(query)
        #### checking/reverse of login
        for username in cursor:
            print(username)
            if username[0] != None:
                print("valid")
                return False