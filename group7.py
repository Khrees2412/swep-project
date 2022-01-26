import sqlite3, datetime

db = sqlite3.connect('users.db')
print("Opened database successfully")

dt = datetime.datetime.today()
year = dt.year

def getMonth(month):
    monthDict = {
    "January": 1,
	"February": 2,
	"March": 3,
	"April": 4,
	"May": 5,
	"June": 6,
	"July": 7,
	"August": 8,
	"September": 9,
	"October": 10,
	"November": 11,
	"December": 12,
    }
    for key in monthDict: 
	    if monthDict[key] == month:
		    return key;	

month = getMonth(dt.month)


print("Welcome to the Lautech Cooperative Society. \n What operation would you like to perform today?")
print("    ")
op_code = int(input(" * Select 1 for registration of a new account \n * Select 2 to deposit/save money to existing account \n * Select 3 for withdrawal of funds \n * Select 4 to take a loan: " ))

def loan():
    print("Loan Selected")
    print("Loans are given with a 10 percent interest rate")
    matric_no = (input("Enter the matric_no of the user: "))
    amount = int(input("Enter the amount you want to loan: "))
    sql = 'SELECT * FROM users WHERE matric_no=? LIMIT 1'
    # cur = db.cursor()
    cursor = db.execute(sql, (matric_no,))
    for item in cursor:
        user = {
    "age": item[2],
    "name": item[1],
    "gender": item[3],
    "address": item[4]      
    }
    name  = user["name"]
    if name:
        sql = 'SELECT amount FROM savings WHERE action=?'
        all_deposits = [cursor[0] for cursor in db.execute(sql, ("deposit",)).fetchall()]
        total = sum(all_deposits)
        if total < amount:
            print("The cooperative can not afford that amount for a loan, request for a lower amount")
        else:
            sqlite_insert(db, "savings", {
                        "amount":amount,
                        "matric_no": matric_no,
                        "name": name,
                        "action":"loan",
                        "year": year,
                        "month": month
                        })
            print("{0} loaned to {1}".format(amount, name))
    else:
        print("{0} does not exist".format(name))

def deposit():
    print("Deposit Selected")
    matric_no = (input("Enter the matric_no of the user: "))
    amount = int(input("Enter the amount you want to deposit: "))
    sql = 'SELECT * FROM users WHERE matric_no=? LIMIT 1'
    cursor = db.execute(sql, (matric_no,))
    for item in cursor:
        user = {
    "age": item[2],
    "name": item[1],
    "gender": item[3],
    "address": item[4]      
    }
    name  = user["name"]
    if user["name"]:
        sqlite_insert(db, "savings", {
            "amount":amount,
            "matric_no": matric_no,
            "name": name,
            "action":"deposit",
            "year": year,
            "month": month
        })
        print("{0} saved for {1}".format(amount, name))
    else:
        print("{0} does not exist".format(name))


def withdraw():
    print("Withdrawal selected")
    matric_no = int(input("Enter the matric_no of the user: "))
    amount = int(input("Enter the amount you want to withdraw: "))
    sql = 'SELECT * FROM users WHERE matric_no=? LIMIT 1'
    cursor = db.execute(sql, (matric_no,))
    for item in cursor:
        user = {
    "age": item[2],
    "matric_no": item[5],
    "gender": item[3],
    "address": item[4],
    "name": item[1]
    }
    if user["matric_no"]:
        print(user)
        sql = 'SELECT * FROM savings WHERE matric_no=? ORDER BY id DESC LIMIT 1'
        row = db.execute(sql, (matric_no,))
        for item in row:
            user = {
            "name": item[1],
            "amount":item[3]
            }
            print(user["name"], "made a withdrawal")
            balance = user["amount"]
            name = user["name"]
            if balance < amount:
                print("Insufficient funds")
            else:
                if user["name"]:
                    sqlite_insert(db, "savings", {
                        "amount":amount,
                        "matric_no": matric_no,
                        "name": name,
                        "action":"withdrawal",
                        "year": year,
                        "month": month
                        })
                print("{0} withdrawn for {1}".format(amount, name))
    else:
        print("{0} does not exist".format(matric_no))


def saveMember(mem):
    memberStr = ' '.join([str(elem) for elem in mem])
    sqlite_insert(db, "COOP_MEMBERS", {
        "members": memberStr
    })


def sqlite_insert(conn, table, row):
    cols = ', '.join('"{}"'.format(col) for col in row.keys())
    vals = ', '.join(':{}'.format(col) for col in row.keys())
    sql = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(table, cols, vals)
    conn.cursor().execute(sql, row)
    conn.commit()
    print("Details saved to database")

def sqlite_select(conn, table, row):
    cols = ', '.join('"{}"'.format(col) for col in row.keys())
    vals = ', '.join(':{}'.format(col) for col in row.keys())
    sql = 'SELECT "{0}" ({1}) VALUES ({2})'.format(table, cols, vals)
    conn.cursor().execute(sql, row)
    conn.commit()
    print("details retrieved from db")

def registration():
    print("registration selected")
    coop_members = []

    def getMembers():
        cursor = db.execute(
        "SELECT * from USERS"
    )
        for item in cursor:
            new_member =  {
        "age": item[2],
        "name": item[1],
        "gender": item[3],
        "address": item[4]
    }
            coop_members.append(new_member)
    print("The members of the cooperative are:", coop_members )
 
    
    def removeMember():
        matric_no = int(input("Enter the matric number of the member you want to remove: "))
        sql = 'DELETE FROM users WHERE matric_no = ?'
        cur = db.cursor()
        cur.execute(sql, (matric_no,))
        db.commit()
        for item in coop_members[:]:
            if item["matric_no"] == matric_no:
                coop_members.remove(item)


    firstname  = str(input("Enter your firstname: "))
    lastname  = str(input("Enter your lastname: "))
    name = firstname + " " + lastname
    address = str(input("Enter your address: "))
    matric_no = input("Enter your matric number: ")
    
    while len(matric_no) < 6:
        print("Matric number must be 6 integers")
        matric_no = input("Enter your matric number: ")

    age = int(input("Enter your age: "))
    gender = input("Select a gender (M or F): ")

    if gender == "M":
        print(gender)
    elif gender == "F":
        print(gender)
    else:
        print("Invalid gender selected. Enter M for Male and F for Female");
        gender = input("Select a gender (M or F): ")
 
    member =  {
        "age": age,
        "name": name,
        "gender": gender,
        "address": address,
        "matric_no": matric_no
    }

# Save a member to the database
    sqlite_insert(db, "users", member)

# Print the list of all registered members
    getMembers()

if op_code == 1:
    registration()
elif op_code == 2:
        deposit()
elif op_code == 3:
        withdraw() 
elif op_code == 4:
        loan()