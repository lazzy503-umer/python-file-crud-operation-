file = open("u.txt", "r")
password = file.readline().strip()
file.close()

print("Welcome to password manager application")
password_input = input("Enter password: ")
if password_input == "Lazzy503":
    check = True
    while check:
        print("1. Get user credentials")
        print("2. Add user credentials")
        print("3. Remove user credentials")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            file = open("database.txt", "r")
            data = file.readlines()
            file.close()
            if len(data) > 0:
                for credential in data:
                    credential = credential.strip().split(",")
                    print(credential[0] + ". " + credential[1])
                account_id = input("Enter account choice(number): ")
                tmp = True
                for credential in data:
                    credential = credential.strip().split(",")
                    if account_id == credential[0]:
                        tmp = False
                        print("Account name:", credential[1])
                        print("User ID:", credential[2])
                        print("Password:", credential[3])
                        break
                if tmp:
                    print("You have entered an invalid choice.")
            else:
                print("No data available.")
        elif choice == "2":
            file = open("database.txt", "r")
            data = file.readlines()
            file.close()
            account_name = input("Enter account name: ")
            user_id = input("Enter user ID: ")
            user_password = input("Enter password: ")
            final_data = str(len(data) + 1) + "," + account_name + "," + user_id + "," + user_password
            file = open("database.txt", "a")
            file.write("\n")
            file.write(final_data)
            file.close()
            print("User credentials have been added successfully.")
        elif choice == "3":
            file = open("database.txt", "r")
            data = file.readlines()
            information = list(data)
            file.close()
            if len(data) > 0:
                for credential in data:
                    credential = credential.strip().split(",")
                    print(credential[0] + ". " + credential[1])
                account_id = input("Enter account choice(number): ")
                tmp = True
                for i in range(len(data)):
                    data[i] = data[i].strip().split(",")
                    if account_id == data[i][0]:
                        tmp = False
                        information.pop(i)
                        break
                if tmp:
                    print("You have entered an invalid choice.")
                file = open("database.txt", "w")
                for line in information:
                    file.write(line)
                file.close()
            else:
                print("No data available.")
        elif choice == "4":
            check = False
else:
    print("Invalid password. Access denied.")
