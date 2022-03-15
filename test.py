from login_class1 import login_menu

login_window = login_menu()

#login_window.get_all_data()
a = (login_window.log_in("Plesniok", "adminadmin"))
print(a == False)

#print(login_window.register("Plesniok123", "adminadmin"))

#print(login_window.register_valid("dad"))