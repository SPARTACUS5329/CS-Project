from pymysql import cursors
import RSA  # ENCRYPTION ALGORITHM
import pymysql as sql
import os

# Connecting to the dabase
while True:
    try:
        passcode = input('ENTER THE PASSWORD:-')
        user_db = sql.connect(host='localhost', user='root',
                              passwd=passcode, db='users')
        user_cursor = user_db.cursor()
        # Creating the table if it doesn't exist
        try:
            user_cursor.execute("""create table users(
                                userid char(20) not null,
                                username char(20) primary key,
                                password char(20)
                            );""")
        except:
            pass
        print("Successfully connected to the database")
        break
    except:
        print('INCORRECT PASSWORD')


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


def clear_shell():  # A function that clears the terminal
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    return None


def retrieve_user_list():
    record_tuples = user_cursor.execute('select * from users;')
    record_tuples = user_cursor.fetchall()
    _user = {}
    for i in record_tuples:
        _user[i[1]] = i[2]
    return _user


def create_account():
    global user_list
    username = input("Enter the username: ")
    if username in user_list:
        print('This username already exists')
        return create_account()
    else:
        userid = input("Enter your userid: ")
        password = input("Enter your password: ")
        user_cursor.execute(
            f"insert into users values('{userid}','{username}','{password}')")
        user_cursor.execute(f"""create table {username}_inbox (
                            sender char(20) not null,
                            message text
                            );""")
        user_cursor.execute(f"""create table {username}_outbox (
                            sender char(20) not null,
                            message text
                            );""")
        user_db.commit()
        user_list = retrieve_user_list()
        print("Account created successfully")
    return None


def login(username):
    password = input("Enter your password: ")
    if not password == user_list[username]:
        print("Incorrect password...")
        return login(username)

    else:
        return True


def send_message(username):
    receiver = input("To: ")
    if receiver not in user_list:
        print("This receiver does not exist")
        return send_message()
    else:
        message = input("Message: ")
        user_cursor.execute(
            f"insert into {receiver}_inbox values('{username}','{message}');")
        user_cursor.execute(
            f"insert into {username}_outbox values('{receiver}','{message}');")
        user_db.commit()
        print("Message sent successfully")
        return True


def check_individual_inbox(username):
    messages = user_cursor.execute(f"select * from {username}_inbox;")
    messages = user_cursor.fetchall()
    for i in messages:
        print(f"{i[0]}: {i[1]}")
        print("\n")
        print("----------------------")
    return None


def check_individual_outbox(username):
    messages = user_cursor.execute(f"select * from {username}_outbox;")
    messages = user_cursor.fetchall()
    for i in messages:
        print(f"{i[0]}: {i[1]}")
        print("\n")
        print("----------------------")
    return None


def login_menu(username):
    clear_shell()
    print("These are all the tasks you can perform")
    print("1.Send a message")
    print("2.Check your individual inbox")
    print("3.Log out")
    print("4.Erase all messages in your inbox")
    print("5.Check your outbox")
    print("6.Create a group")
    print("7.Check your group inbox")
    choice = input("Enter your choice: ")
    if choice == '1':
        send_message(username)
    elif choice == '2':
        check_individual_inbox(username)
    elif choice == '3':
        return None
    elif choice == '5':
        check_individual_outbox(username)
    else:
        print("Enter a valid option")
    input("Press enter to continue...")
    return login_menu(username)


def Menu():
    clear_shell()
    print("Choose what you want to do: ")
    print("1.Create an account")
    print("2.Login")
    print("3.Exit")
    response = input("Enter your response: ")
    if response == "1":
        create_account()
    elif response == "2":
        username = input("Enter your username: ")
        if username not in user_list:
            print("This username doesn't exist...")
            print("Try creating an account: ")
        else:
            if (login(username)):
                login_menu(username)
    elif response == "3":
        user_cursor.close()
        user_db.close()
        exit()
    else:
        print("Invalid response")
    input("Press Enter to continue...\n\n")
    Menu()


if __name__ == "__main__":
    user_list = retrieve_user_list()
    Menu()
