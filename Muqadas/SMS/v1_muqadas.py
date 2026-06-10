# student
# admin

# DATABASE

# student_1
roll_no_1 = None
std_name_1 = None
std_fee_1 = None
std_password_1 = None
std_role_1 = None

# student_2
roll_no_2 = None
std_name_2 = None
std_fee_2 = None
std_password_2 = None
std_role_2 = None

# student_3
roll_no_3 = None
std_name_3 = None
std_fee_3 = None
std_password_3 = None
std_role_3 = None

# admin
admin_username = 'Azan'
admin_password = 'admin'
admin_role = 'admin'

# login features
username = input("Enter your username -> ")
password = input("Enter your password -> ")
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
    current_user_role = admin_role
else:
    print("invalid username or password")

if (current_user_role == admin_role):
    print()
    print("-----Admin_Main_Menu-----")
    print()
    print("1 - Add student")
    print("2 - View students")
    print("3 - Search Student")
    print("4 - Update Student")
    print("5 - Delete Student")
    print("6 - View sorted student")
    print()
    print("-----Choose_one_option-----")
    choosen_one_option = int(input("choose_option -> "))
    print()
    if (choosen_one_option == 1):


        print("-----Add student-----")
        print()
        std_roll_no = input("Enter student roll no -> ")
        std_name = input("Enter student name -> ")
        std_password = input("Enter student password -> ")
        std_fee = int(input("Enter student fee -> "))

        roll_no_1 = std_roll_no
        std_name_1 = std_name
        std_fee_1 = std_fee
        std_password_1 = std_password
        std_role_1 = 'student'

    elif (choosen_one_option == 2):
        print("-----View students-----")
        print()
        print("Roll Number    |Name      |Fee")
        print(f"{roll_no_1}   |{std_name_1}    |{std_fee_1}")
        print(f"{roll_no_2}   |{std_name_2}    |{std_fee_2}")
        print(f"{roll_no_3}   |{std_name_3}    |{std_fee_3}")

    elif (choosen_one_option == 3):
        print("-----Search student-----")
        print()
    elif (choosen_one_option == 4):
        print("-----Update student-----")
        print()
    elif (choosen_one_option == 5):
        print("-----Delete student-----")
        print()
    elif (choosen_one_option == 6):
        print("-----View sorted student-----")
        print()

if (current_user_role == admin_role):
    print()
    print("-----Admin_Main_Menu-----")
    print()
    print("1 - Add student")
    print("2 - View students")
    print("3 - Search Student")
    print("4 - Update Student")
    print("5 - Delete Student")
    print("6 - View sorted student")
    print()
    print("-----Choose_one_option-----")
    choosen_one_option = int(input("choose_option -> "))
    print()
    if (choosen_one_option == 1):


        print("-----Add student-----")
        print()
        std_roll_no = input("Enter student roll no -> ")
        std_name = input("Enter student name -> ")
        std_password = input("Enter student password -> ")
        std_fee = int(input("Enter student fee -> "))

        roll_no_1 = std_roll_no
        std_name_1 = std_name
        std_fee_1 = std_fee
        std_password_1 = std_password
        std_role_1 = 'student'

    elif (choosen_one_option == 2):
        print("-----View students-----")
        print()
        print("Roll Number    |Name      |Fee")
        print(f"{roll_no_1}   |{std_name_1}    |{std_fee_1}")
        print(f"{roll_no_2}   |{std_name_2}    |{std_fee_2}")
        print(f"{roll_no_3}   |{std_name_3}    |{std_fee_3}")

    elif (choosen_one_option == 3):
        print("-----Search student-----")
        print()
    elif (choosen_one_option == 4):
        print("-----Update student-----")
        print()
    elif (choosen_one_option == 5):
        print("-----Delete student-----")
        print()
    elif (choosen_one_option == 6):
        print("-----View sorted student-----")
        print()


if (current_user_role == admin_role):
    print()
    print("-----Admin_Main_Menu-----")
    print()
    print("1 - Add student")
    print("2 - View students")
    print("3 - Search Student")
    print("4 - Update Student")
    print("5 - Delete Student")
    print("6 - View sorted student")
    print()
    print("-----Choose_one_option-----")
    choosen_one_option = int(input("choose_option -> "))
    print()
    if (choosen_one_option == 1):


        print("-----Add student-----")
        print()
        std_roll_no = input("Enter student roll no -> ")
        std_name = input("Enter student name -> ")
        std_password = input("Enter student password -> ")
        std_fee = int(input("Enter student fee -> "))

        roll_no_1 = std_roll_no
        std_name_1 = std_name
        std_fee_1 = std_fee
        std_password_1 = std_password
        std_role_1 = 'student'

    elif (choosen_one_option == 2):
        print("-----View students-----")
        print()
        print("Roll Number    |Name      |Fee")
        print(f"{roll_no_1}   |{std_name_1}    |{std_fee_1}")
        print(f"{roll_no_2}   |{std_name_2}    |{std_fee_2}")
        print(f"{roll_no_3}   |{std_name_3}    |{std_fee_3}")

    elif (choosen_one_option == 3):
        print("-----Search student-----")
        print()
    elif (choosen_one_option == 4):
        print("-----Update student-----")
        print()
    elif (choosen_one_option == 5):
        print("-----Delete student-----")
        print()
    elif (choosen_one_option == 6):
        print("-----View sorted student-----")
        print()


if (current_user_role == admin_role):
    print()
    print("-----Admin_Main_Menu-----")
    print()
    print("1 - Add student")
    print("2 - View students")
    print("3 - Search Student")
    print("4 - Update Student")
    print("5 - Delete Student")
    print("6 - View sorted student")
    print()
    print("-----Choose_one_option-----")
    choosen_one_option = int(input("choose_option -> "))
    print()
    if (choosen_one_option == 1):


        print("-----Add student-----")
        print()
        std_roll_no = input("Enter student roll no -> ")
        std_name = input("Enter student name -> ")
        std_password = input("Enter student password -> ")
        std_fee = int(input("Enter student fee -> "))

        roll_no_1 = std_roll_no
        std_name_1 = std_name
        std_fee_1 = std_fee
        std_password_1 = std_password
        std_role_1 = 'student'

    elif (choosen_one_option == 2):
        print("-----View students-----")
        print()
        print("Roll Number    |Name      |Fee")
        print(f"{roll_no_1}   |{std_name_1}    |{std_fee_1}")
        print(f"{roll_no_2}   |{std_name_2}    |{std_fee_2}")
        print(f"{roll_no_3}   |{std_name_3}    |{std_fee_3}")

    elif (choosen_one_option == 3):
        print("-----Search student-----")
        print()
    elif (choosen_one_option == 4):
        print("-----Update student-----")
        print()
    elif (choosen_one_option == 5):
        print("-----Delete student-----")
        print()
    elif (choosen_one_option == 6):
        print("-----View sorted student-----")
        print()



if (current_user_role == admin_role):
    print()
    print("-----Admin_Main_Menu-----")
    print()
    print("1 - Add student")
    print("2 - View students")
    print("3 - Search Student")
    print("4 - Update Student")
    print("5 - Delete Student")
    print("6 - View sorted student")
    print()
    print("-----Choose_one_option-----")
    choosen_one_option = int(input("choose_option -> "))
    print()
    if (choosen_one_option == 1):


        print("-----Add student-----")
        print()
        std_roll_no = input("Enter student roll no -> ")
        std_name = input("Enter student name -> ")
        std_password = input("Enter student password -> ")
        std_fee = int(input("Enter student fee -> "))

        roll_no_1 = std_roll_no
        std_name_1 = std_name
        std_fee_1 = std_fee
        std_password_1 = std_password
        std_role_1 = 'student'

    elif (choosen_one_option == 2):
        print("-----View students-----")
        print()
        print("Roll Number    |Name      |Fee")
        print(f"{roll_no_1}   |{std_name_1}    |{std_fee_1}")
        print(f"{roll_no_2}   |{std_name_2}    |{std_fee_2}")
        print(f"{roll_no_3}   |{std_name_3}    |{std_fee_3}")

    elif (choosen_one_option == 3):
        print("-----Search student-----")
        print()
    elif (choosen_one_option == 4):
        print("-----Update student-----")
        print()
    elif (choosen_one_option == 5):
        print("-----Delete student-----")
        print()
    elif (choosen_one_option == 6):
        print("-----View sorted student-----")
        print()