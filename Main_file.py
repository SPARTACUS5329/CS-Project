import userdata  # This is the file that has all the details about all the users
import pickle  # Library for handling binary files
import RSA  # File that has the encryption algorithm ie RSA that is being used for storing messages
import importlib  # Library that is used to reload a particular file in this case userdata so that everything can be handled in real time
import os  # Library for handling the terminal
import pymysql as sql

try:  # Checking if the module colorama already exists
    import colorama
except:  # Handling the exception according to the operating system
    if os.name == 'posix':
        os.system('pip3 install colorama')
    elif os.name == 'nt':
        os.system('pip insall colorama')
    else:
        print("What on Earth are you doing?")
    import colorama  # Importing colorama once it is done
finally:  # Initialisng colorama and it's elements
    from colorama import Fore, Back, Style
    colorama.init()


# Connecting to the database
while True:
    try:
        passcode = input('ENTER THE PASSWORD:-')
        user_workspace = sql.connect(host='localhost', user='root',
                                     passwd=passcode)
        cursor = user_workspace.cursor()
        try:
            cursor.execute('create database users;')
        finally:
            cursor.execute('use users;')
            #Creating the table
            cursor.execute("""create table users(
                              userid char(20) not null,
                              username char(20) primary key,
                              password char(20)
                            );""")
        break
    except:
        print('INCORRECT PASSWORD')


def doNothing(*args):  # A function used while development
    pass

def hazh(x):  # Hashing function that is used to store passowrds
    sume = sumo = suma = pr4 = pr3 = 0
    ods = evs = prall = 1
    for i in range(0, len(x), 2):
        sume += ord(x[i])
    for i in range(1, len(x), 2):
        sumo += ord(x[i])
    for i in range(len(x)):
        prall *= ord(x[i])+i
    for i in range(0, len(x), 4):
        pr4 += (ord(x[i]) * ord(x[i-1]) * ord(x[i-2]) * ord(x[i-3]))
    for i in range(0, len(x), 3):
        pr3 += (ord(x[i]) * ord(x[i-1]) * ord(x[i-2]))
    for i in range(1, len(x), 2):
        ods *= ord(x[i])
    for i in range(0, len(x), 2):
        evs *= ord(x[i])
    # for i in range(0,len(x),2):
    prs = hex(sume*sumo)[-1:-3:-1]
    suma = (sume+sumo)*len(x) - sume
    suma = hex(suma)[-1:-3:-1]
    if ods > evs:
        oediff = ods-evs
    else:
        oediff = ods + evs
    while not oediff % 16:
        oediff //= 16
    oediff = hex(oediff)[-1:-3:-1]
    while not prall % 16:
        prall //= 16
    prall = hex(prall)[-1:-5:-1]
    pr43 = hex(pr4 % pr3)[-1:-3:-1]
    result = prall+suma+oediff+prs+pr43

    return result


def reset_colorama_settings():  # Function for resetting all changes in the terminal colors
    print(Fore.RESET)
    print(Back.RESET)
    print(Style.RESET_ALL)
    return None


def clear_shell():  # A function that clears the terminal
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    return None


def create_account():
    username = input("Enter your username: ")
    if username in userdata.userDict:
        print("Username already exists, enter a new one\n\n")
        create_account()
    else:
        password1 = input("Enter your password: ")
        password = hazh(password1)
        with open("userdata.py", 'a') as f:
            write_text = "\nuserDict['"+username+"'] = '"+password+"'"
            f.write(write_text)
        inbox_filename = "./UserfilesInbox/"+username+".dat"
        outbox_filename = "./UserfilesOutbox/"+username+".dat"
        inbox_userfile = open(inbox_filename, 'w')
        inbox_userfile.close()
        outbox_userfile = open(outbox_filename, 'w')
        outbox_userfile.close()
        importlib.reload(userdata)
        login(username, password1)


def send(username):
    receiver = input("To(Group's name/individual's name): ")
    if receiver in userdata.userDict:
        receiver_file = "./UserfilesInbox/"+receiver+".dat"
        sender_file = "./UserfilesOutbox/"+username+".dat"
        message = username+": "+input("Enter message: ")
        KEY_r = userdata.userDict[receiver]
        KEY_s = userdata.userDict[username]
        message_r = RSA.rsa(message, RSA.keys(KEY_r, True)[
                            0], RSA.keys(KEY_r, True)[1], True)
        with open(receiver_file, 'ab') as f:
            pickle.dump(message_r, f)
        message_s = RSA.rsa(message, RSA.keys(KEY_s, True)[
                            0], RSA.keys(KEY_s, True)[1], True)
        with open(sender_file, 'ab') as f:
            pickle.dump(message, f)
        print("Message sent")

    elif receiver in userdata.groupDict:
        group_password = input("Enter the password of the group: ")
        group_password = hazh(group_password)
        if userdata.groupDict[receiver] == group_password:
            receiver_file = "./Groups/"+receiver+".dat"
            sender_file = "./UserfilesOutbox/"+username+".dat"
            message = username+": "+input("Enter message: ")
            with open(receiver_file, 'ab') as f:
                message1 = RSA.rsa(message, RSA.keys(group_password, True)[
                                   0], RSA.keys(group_password, True)[1], True)
                pickle.dump(message1, f)

            KEY = userdata.userDict[username]

            with open(sender_file, 'ab') as f:
                message2 = RSA.rsa(message, RSA.keys(KEY, True)[
                                   0], RSA.keys(KEY, True)[1], True)
                pickle.dump(message2, f)
            print("Message sent")
        else:
            print("Incorrect password")
            send()

    else:
        print("This receiver does not exist.")
        send(username)


def check_inbox(username):
    filename = "./UserfilesInbox/"+username+".dat"
    KEY = userdata.userDict[username]
    with open(filename, 'rb') as f:

        try:
            while True:
                messagelist = pickle.load(f)
                messagelist = RSA.rsa(messagelist, RSA.keys(KEY, False)[
                                      0], RSA.keys(KEY, False)[1], False)
                print(Fore.RED + messagelist)
                print(Fore.WHITE + "_"*20)
                reset_colorama_settings()
        except:
            pass


def clear_messages(username):
    filename = "./UserfilesInbox/"+username+".dat"
    with open(filename, 'wb') as f:
        pickle.dump('', f)


def check_outbox(username):
    outbox_filename = "./UserfilesOutbox/"+username+".dat"
    with open(outbox_filename, 'rb') as f:
        try:
            while True:
                messagelist = pickle.load(f)
                print(Fore.RED)
                print(messagelist)
                reset_colorama_settings()
        except:
            pass


def create_group(group_list, admin):
    print(Fore.RED)
    group_name = input("Name of the group: ")
    if group_name in userdata.groupDict:
        print("This group name already exists, try choosing a different one")
        create_group(group_list, admin)
    else:
        group_password = input("Password of group: ")
        reset_colorama_settings()
        group_password_text = group_password
        group_password = hazh(group_password)
        for user in group_list:
            user_file = "./UserfilesInbox/"+user+".dat"
            message = "A new group called "+group_name+" has been created by " + \
                admin+" and the password is "+group_password_text
            KEY = userdata.userDict[user]
            message = RSA.rsa(message, RSA.keys(KEY, True)[
                              0], RSA.keys(KEY, True)[1], True)
            with open(user_file, 'ab') as f:
                pickle.dump(message, f)
        with open("userdata.py", 'a') as f:
            write_text = "\ngroupDict['"+group_name+"'] = '"+group_password+"'"
            f.write(write_text)
        importlib.reload(userdata)

    group_path = "./Groups/"+group_name+".dat"
    with open(group_path, 'wb') as f:
        message = "A new group called "+group_name+" has been created by "+admin
        message = RSA.rsa(message, RSA.keys(group_password, True)[
                          0], RSA.keys(group_password, True)[1], True)
        pickle.dump(message, f)

    check_group_inbox(group_name, True)


def check_group_inbox(group_name, newGroup):
    if not newGroup:
        group_password = input("Enter the password: ")
        group_password = hazh(group_password)
        if userdata.groupDict[group_name] == group_password:
            group_path = "./Groups/"+group_name+".dat"
            with open(group_path, 'rb') as f:
                try:
                    while True:
                        message = pickle.load(f)
                        message = RSA.rsa(message, RSA.keys(group_password, False)[
                                          0], RSA.keys(group_password, False)[1], False)
                        print(Fore.RED+message)
                        print(Fore.WHITE+"_"*20)
                        reset_colorama_settings()
                except:
                    pass
        else:
            print("The password is incorrect, try again")
            check_group_inbox(group_name, False)

    else:
        group_path = "./Groups/"+group_name+".dat"
        with open(group_path, 'rb') as f:
            try:
                while True:
                    message = pickle.load(f)
                    print(Fore.RED+message)
                    print(Fore.WHITE+"_"*20)
                    reset_colorama_settings()
            except:
                pass


def loginMenu(username):
    clear_shell()
    print(Fore.GREEN)
    print("\n\n\n\n")
    print("These are all the tasks you can perform: ")
    print("1.Send a message")
    print("2.Check your individual inbox")
    print("3.Log out")
    print("4.Erase all messages in your inbox")
    print("5.Check your outbox")
    print("6.Create a group")
    print("7.Check your group inbox")
    print(Fore.RED)
    print(Back.WHITE)
    print(Style.BRIGHT)
    response = input("Enter your response: ")
    reset_colorama_settings()
    if response == "1":
        send(username)
    elif response == "2":
        check_inbox(username)
    elif response == "3":
        return
    elif response == "4":
        clear_messages(username)
    elif response == "5":
        check_outbox(username)
    elif response == "6":
        number_of_members = int(
            input("How many members do you want in the group: "))
        group_list = []
        i = 0
        while i < number_of_members:
            user = input("Enter the name of member "+str(i+1)+": ")
            if user in userdata.userDict:
                group_list.append(user)
                i += 1
            else:
                print("This member does not exist")
                print("Try again\n\n")
        create_group(group_list, username)
    elif response == "7":
        group_name = input("Enter the name of the group you want to check: ")
        check_group_inbox(group_name, False)
    else:
        print("Invalid input")
    input("Press Enter to continue...\n\n")
    loginMenu(username)


def login(username, password):
    password = hazh(password)
    if userdata.userDict[username] == password:
        loginMenu(username)
    else:
        print("Wrong password")
        password = input("Enter the password: ")
        login(username, password)


def Menu():
    clear_shell()
    print(Fore.WHITE)
    print("\n\n\nChoose what you want to do: ")
    print("1.Create an account")
    print("2.Login")
    print("3.Exit")
    response = input("Enter your response: ")
    if response == "1":
        create_account()
    elif response == "2":
        username = input("Enter your username: ")
        if username in userdata.userDict:
            password = input("Enter your password: ")
            login(username, password)
        else:
            print("\n\nThis account doesn't exist")
            print("Try entering a valid username or create an account by this name")
    elif response == "3":
        cursor.close()
        user_workspace.close()
        exit()
    else:
        print("Invalid response")
    input("Press Enter to continue...\n\n")
    Menu()


def terminal_check(using_terminal):
    if using_terminal == 'y' or using_terminal == 'Y' or using_terminal == 'Yes' or using_terminal == 'yes':
        return None
    elif using_terminal == 'n' or using_terminal == 'N' or using_terminal == 'No' or using_terminal == 'no':
        if os.name == 'posix':
            os.system('open /System/Applications/Utilities/Terminal.app')
            os.chdir('.')
            os.system('Python3.8 Main_file.py')
        elif os.name == 'nt':  # Add code here for opening cmd
            os.system('')
            os.chdir('.')
            os.system('python Main_file.py')
        else:
            print("What on Earth are you doing?")
        exit()
    else:
        print("Enter a valid answer")
        return terminal_check(using_terminal)


if __name__ == "__main__":
    using_terminal = input("Are you using the Terminal/Command Prompt(y/n) ? ")
    terminal_check(using_terminal)
    Menu()
