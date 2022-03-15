

def login_menu_f():
    from login_class1 import login_menu
    login_window = login_menu()
    while True:
        declaration = input("1.login \n2.register\nq, aby zakończyć\n")
        if declaration == "1":
            return login_window.log_in()
                
        elif declaration == "2":
            while True:
                return login_window.register()
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
