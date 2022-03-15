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
    
    def log_in(self, cursor = cursor):
        """funkcja zwraca nazwe użytkownika jeśli istnieje"""
        while True:
            username = input("podaj nazwę użytkownika\n")
            password = input("podaj hasło\n")
            
            query = f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}';"
            cursor.execute(query)
            #### checking
            for id in cursor:
                if id[0] == None:
                    return False
                else:
                    print(f"witaj: {username}!")
                    return True
            print("błędne dane użytkownika")

    
    def register_valid(self, new_username):
        """funkcja zwraca None, jeśli nie ma duplikatów,
        False jeśli występują"""
        cursor = self.connection.cursor()
        query = f"SELECT username FROM users WHERE username = '{new_username}';"
        cursor.execute(query)
        #### checking/reverse of login
        for username in cursor:
            if username[0] != None:
                return False
    
    def register(self,register_valid = register_valid,cursor = cursor):
        """funkcja wprowadza dane użytkownika do bazy danych
        oraz printuje jeśli się udało"""
        while True:
            new_username = input("podaj nazwę użytkownika\n")
            new_password = input("podaj hasło\n")
            if register_valid(self, new_username) == False:
                print("niestety uzytkownik o podanej nazwie juz istnieje")
            else:
                insertQuery = "INSERT INTO users(username, password) VALUES (%(username)s, %(password)s);"
                insert_data = {'username' : new_username, 'password' : new_password}
                cursor.execute(insertQuery, insert_data)

                self.connection.commit()
                print(f"witaj: {new_username}!")
                return True
    
    ### nie wiem czemu wczesniej cursor
    # w argumencie działał, a w tym przypadku nie działa