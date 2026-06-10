# 3 students
# 1 Admin

# student_1
roll_no_1 = None
std_name_1 = None
std_fee_1 = None
std_role_1 = None
std_password_1 = None

# student_2
roll_no_2 = None
std_name_2 = None
std_fee_2 = None
std_role_2 = None
std_password_2 = None

# student_3
roll_no_3 = None
std_name_3 = None
std_fee_3 = None
std_role_3 = None
std_password_3 = None

# Admin
admin_name = "Azan"
admin_username = "admin"
admin_password = "admin"
role_admin = 'admin'


# Driver code

#login_feature

username = input("Enter your username-> ")
password = input("Enter your password-> ")

current_user = None
current_user_role = None
if (username == roll_no_1 and password == std_password_1):
    current_user = roll_no_1
    current_user_role = std_role_1

elif (username == roll_no_2 and password == std_password_2):
    current_user = roll_no_2
    current_user_role = std_role_2

elif (username == roll_no_3 and password == std_password_3):
    current_user = roll_no_3
    current_user_role = std_role_3

elif (username == admin_username and password == admin_password):
    current_user = admin_username
    current_user_role = role_admin

else:
    print("invalid username or password")

#Displaying Menu

if current_user_role == role_admin:
    print("Admin Main Menu")
    print()
    print("1 - Add student")
    print("2 - View students")
    print("3 - Search Student")
    print("4 - Update Student")
    print("5 - Delete Student")
    print("6 - View sorted student")

    main_menu_choosen_option = input("Choose Option") 

    if main_menu_choosen_option == '1':
        #input student info
        





