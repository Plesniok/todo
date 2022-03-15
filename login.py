from login_class1 import login_menu

def login_menu_f():
    login_window = login_menu()
    while True:
        declaration = input("1.login \n2.register\nq, aby zakończyć\n")
        if declaration == "1":
            while True:
                input_user = input("podaj nazwę użytkownika\n")
                input_password = input("podaj hasło\n")
                
                condition = (login_window.log_in(input_user, input_password))
                if condition == True:
                    return input_user
                else:
                    print("błędne dane\n")
        elif declaration == "2":
            while True:
                input_user = input("podaj nazwę użytkownika\n")
                input_password = input("podaj hasło\n")
                
                condition = (login_window.register(input_user, input_password))
                if condition == True:
                    return input_user
                else:
                    print("użytkownik o podanej nazwie już istnieje\n")
        elif declaration == "q":
            break
        else:
            print("błędna deklaracja\n")
            continue

login_menu_f()


#login_window.get_all_data()

#print(login_window.log_in("Plesniok", "adminadmin"))

#print(login_window.register("Plesniok123", "adminadmin"))

#print(login_window.register_valid("dad"))
