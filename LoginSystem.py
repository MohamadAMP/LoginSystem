import sqlite3
import openpyxl
import Functions as f
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

filepath = "C:/Users/Mohamad/Desktop/LoginSystem/Expenses.xlsx"
wb = openpyxl.load_workbook(filepath)

print("Hello! Thank you for using ... to organize your day and track your expenses!")
login_verification = input("If your new here and you want to create an account, please type yes. If you already have an account type no: ")
print("\n")

if login_verification == 'yes':
    first_Name = input("Please enter your first name: ")
    last_Name = input("Please enter your last name: ")
    _email = input("Please enter your email address: ")
    _password = input("Please enter your password: ")
    new_data = ("INSERT INTO accounts (firstName, lastName, email, password) VALUES ('{}', '{}', '{}', '{}');".format(first_Name, last_Name, _email, _password))
    c.execute(new_data)
    conn.commit()
    c.execute("SELECT * FROM accounts WHERE email = (?)", (_email,))
    current = c.fetchone()
    wb.create_sheet(current[2] + "'s Expenses")
    wb.save("Expenses.xlsx")
    print("Please log in to start using your account\n")

access = True
c.execute("SELECT * FROM accounts")
q = c.fetchall()
while access:
    _email = input("Please enter your email address: ")
    _password = input("Please enter your password: ")
    print("\n")
    verified = f.accountVerification(q, _email, _password)
    if verified == True:
        c.execute("SELECT * FROM accounts WHERE email = (?)", (_email,))
        current = c.fetchone()
        access = False
    else:
        print("You entered the wrong login details. Please try again.")

v = True
while v:
    section = f.homeScreen()
    print("\n")

    if section == 'tasks' or section == 'Tasks':
        fileName = current[2] + "'s Tasks.txt"
        m = True
        while m:
            action = f.tasksHomeScreen()
            print('\n')
            if action == '1':
                f.tasks1(fileName)
            elif action == '2':
                f.tasks2(fileName)
            elif action == '3':
                f.tasks3(fileName)
            else:
                m = False

    elif section == 'expenses' or section == 'Expenses':
        sheetName = (current[2] + "'s Expenses")
        m = True
        while m:
            action = f.expensesHomeScreen()
            print('\n')
            if action == '1':
                f.expenses1(sheetName)
            elif action == '2':
                f.expenses2(sheetName)
            else:
                m = False

#c.execute(("SELECT * FROM accounts"))
#print(c.fetchall())
wb.save("Expenses.xlsx")

conn.commit()
conn.close()