#import all the necessary libraries

import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd

#establishing mysql connection 
mydb=mysql.connector.connect(user = 'root',
                     passwd = 'Ak@050804',
                     host = 'localhost',
                     auth_plugin = 'mysql_native_password',
                     database = 'BankDBMS')

mycursor=mydb.cursor(buffered=True)

#Created Database BankDBMS
#mycursor.execute('create database BankDBMS;')

#defining various user_defined functions

#LOGIN - function to enter the database
#Login table creation
def login_table():
    try:
        mycursor.execute('create table LOGIN(ACCNO varchar(10),NAME varchar(30),LOGIN_ID varchar(10),LOGIN_PSWD char(10));')
        
        print("Table Created") 
        
        login_details()
        
    except:
        print("Table Exist") 
        
        login_details()
        

def login_details(): #Function to enter login details for storage

    while True:	#Loop for accepting records 
    
        Name=input("Enter Name : ")
        
        login_id =input("Enter Login ID : ")
        
        print("NOTE : Your login password should be of 10 characters or less")
        lpswd =input("Enter Login password :") 
        
        Rec2 =[Name.upper(),login_id,lpswd]
        Cmd2 ="insert into LOGIN values(%s,%s,%s)" 
        
        mycursor.execute(Cmd2,Rec2)
        mydb.commit()

        break
    
def Login_check():	#Function to check details of the customer login
    try:
        cmd="select * from LOGIN" 
        
        mycursor.execute(cmd) 
        S=mycursor.fetchall()
        
        Name=input("Enter Name : ")
        print(Name)
        
        login_id =input("Enter Login ID : ")

        print("NOTE : Your login password should be of 10 characters or less")
        lpswd =input("Enter Login password :") 
        print(lpswd)

        for i in S:
            
            i=list(i)
            
            if i[1] == login_id :
                
                print("..Thank You for logging in..")
                
                break
 
        else:
            print("!!.....RECORD NOT FOUND…..!!")
            Login_check()
    except:
        print(".....NO SUCH TABLE EXISTS.....")
        

print("...................................................................................................................")
print("\n")

log = input("Welcome,Already have an account in our system..? yes(y)/no(n) : ")

if log in ["y","Y"]:
    print("You will be directed to our login page")
    
    print("\n")
    
    print("___________________________________________________________________________________________________________".center(140))
    print("LOGIN TO THE DATABASE".center(140))
    print("___________________________________________________________________________________________________________".center(140))
    Login_check()

elif log in ["n","N"]:
    print("..Welcome New user.. Please register to our system")
    
    login_details()
    
else:
    print("Invalid choice...Try Again")
    login_table()

 

#Printing some messages for the user
print("______________________________________________________________________________".center(140))
print("                        WELCOME TO GOLDEN HORIZON BANK                        ".center(140))
print("______________________________________________________________________________".center(140))
print("                          We Understand Your World                            ".center(140))
print("______________________________________________________________________________".center(140))
print()

print("GOLDEN HORIZON BANK is one of India’s leading private banks.".center(140))
print()
    
print("Today, GOLDEN HORIZON BANK has a banking network of 5,653 branches and 16,291".center(140))
print("ATM'sin 2,917 cities/towns.".center(140))

print()

print("..............................................................................".center(140))
print(".                         ..ALL YOU NEED TO KNOW..                            ".center(140))
print("..............................................................................".center(140))
print(".  (1) Save paper by going digital                                           .".center(140))
print(".  (2) Be assured of highest levels of security                              .".center(140))
print(".  (3) Enjoy banking services without leaving home                           .".center(140))
print(".  (4) We are happy to bring to you our all new MobileBanking App.           .".center(140))
print(".  (5) Register once, and receive statements automatically every month       .".center(140))
print("..............................................................................".center(140))


#Bank overview with the help of the chart
print("______________________________________________________________________________")
print("BANK OVERVIEW")
print("______________________________________________________________________________")


Data = {'Years': [2015,2016,2017,2018,2019,2020,2021,2022],
        'Profit in (US million dollars)': [12.3,14.5,18.9,21.5,22.8,25.6,27.0,27.4]}
  
df = pd.DataFrame(Data,columns=['Years','Profit in (US million dollars)'])
print(df)

print("\n")
  
plt.title('Bank Profit overview', fontsize=14)

plt.xlabel('Years', fontsize=13)
plt.ylabel('Profit (in US million dollars)', fontsize=13)

plt.plot(df['Years'],df['Profit in (US million dollars)'], color='red', marker='o',linewidth = 3,markersize = 5)
plt.grid(True)


plt.show()

print("______________________________________________________________________________")

print("\n")

input("!...PRESS ENTER...!")

print("\n")

print("______________________________________________________________________________")


def Menu(): #Defining the main menu of the system
    
    print(".............................................")
    print(".                MAIN MENU                  .")
    print(".............................................")
    print(".1. OPEN A NEW ACCOUNT                      .")
    print(".2. DISPLAY RECORDS                         .")
    print(".   A. SORTED AS PER ACCOUNT NUMBER         .")
    print(".   B. SORTED AS PER CUSTOMER NAME          .")
    print(".   C. SORTED AS PER CUSTOMER BALANCE       .")
    print(".3. SEARCH A RECORD AS PER ACCOUNT NUMBER   .")
    print(".4. UPDATE AN EXISTING RECORD               .")
    print(".5. CLOSE/DELETE AN EXISTING RECORD         .")
    print(".6. TRANSACTIONS FROM AN ACCOUNT            .")
    print(".   A. DEBIT/WITHDRAW FROM AN ACCOUNT       .")
    print(".   B. CREDIT INTO AN ACCOUNT               .")
    print(".   C. TRANSFER BETWEEN ACCOUNT             .")
    print(".7. FIXED DEPOSIT CALCULATION               .")
    print(".8. LOAN                                    .")
    print(".   A. HOME LOAN                            .")
    print(".   B. PERSONAL LOAN                        .")
    print(".9. CONSUMER DURABLE LOAN                   .")
    print(".10. EXIT                                   .")
    print(".............................................")
    
def MenuSort(): #Function for choice for sorting of account
    print("	a. Sorted as per Account Number") 
    print("	b. Sorted as per Customer Name") 
    print("	c. Sorted as per Customer Balance") 
    print("	d. Back")

def MenuTransaction(): #Function for choice for transaction in an account
    print("	a. Debit/Withdraw from the account") 
    print("	b. Credit into the account")
    print("	c. Transfer money into accounts") 
    print("	d. Back")

def MenuLoan():
    print("	a. Home Loan") 
    print("	b. Personal Loan")
    print("	c. Back")
# BANK - The basic table of the system

def Create(): #Function that creates and checks for table bank
    try:
        mycursor.execute('create table bank(ACCNO varchar(10),NAME varchar(30),MOBILE_NO char(10),EMAIL_ID varchar(40),ADDRESS varchar(50),CITY varchar(30),COUNTRY varchar(30),BALANCE float(10,3))')
        
        print("Table Created") 
        
        Insert()
    except:
        print("Table Exist") 
        
        Insert()

def Insert(): #Data insertion in Bank

    while True:	#Loop for accepting records 
    
        Acc=input("Enter account number :") 
        
        Name=input("Enter Name : ")
        
        Mob=input("Enter Mobile number : ")
        
        email=input("Enter Email ID : ") 
        
        Add=input("Enter complete Address :") 
        
        City=input("Enter City :") 
        
        Country=input("Enter Country :") 
        
        Bal=float(input("Enter Balance amount : "))
        
        print("To keep your account protected, Please enter a desired password")
        
        Pswd=int(input("Enter Desired Pin: "))
        
        print("PIN code",Pswd," is created")
        
        print("\n")
        
        print("!!.....PLEASE REMEMBER YOUR ACCOUNT NUMBER AND PIN .....!! ")

        Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
        Cmd="insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s)" 
        
        mycursor.execute(Cmd,Rec)
        mydb.commit()
        
        ch=input("Do you want to enter more records ? (y/n)") 
        if ch=='N' or ch=='n':
            break
                
    
def DispSortAcc():	#Function to Display records as per ascending order of Account Number
    try:
        cmd="select * from BANK order by ACCNO ;" 
        
        mycursor.execute(cmd) 
        S=mycursor.fetchall()
        
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        
        print(F % ("ACCNO","NAME","MOBILE NUMBER","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
        
        print("="*150) 
        
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
 
        print() 
        
        print("="*150)
        
    except:
        print("Table doesn't exist")
        
def DispSortName():	#Function to Display records as per ascending order of Name
    try:
        cmd="select * from BANK order by NAME;" 
        
        mycursor.execute(cmd) 
        S=mycursor.fetchall()
        
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        
        print(F % ("ACCNO","NAME","MOBILE NUMBER","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
        
        print("="*150) 
        
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
 
        print() 
        
        print("="*150)
        
    except:
        print("Table doesn't exist")
        
def DispSortBal():	#Function to Display records as per ascending order of Balance
    try:
        cmd="select * from BANK order by BALANCE ;" 
        
        mycursor.execute(cmd) 
        S=mycursor.fetchall()
        
        F="%15s %15s %15s %15s %15s %15s %15s %15s"
        
        print(F % ("ACCNO","NAME","MOBILE NUMBER","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
        
        print("="*150) 
        
        for i in S:
            for j in i:
                print("%14s" % j, end=' ')
 
        print() 
        
        print("="*150)
    except:
        print(".....NO SUCH TABLE EXISTS.....")
        
def DispSearchAcc(): #Function to Search for the Record from the File with respect to the account number
    try:
        cmd="select * from BANK" 
        
        mycursor.execute(cmd) 
        S=mycursor.fetchall()
        
        ch=input("Enter the account no to be searched : ") 
        p02 = int(input("Enter your password : "))
        print(p02)
        
        for i in S:

            if i[0]==ch:
        
                print("="*150)
                
                F="%15s,%15s,%15s,%15s,%15s,%15s,%15s,%15s"
                print(F % ("ACCNO","NAME","MOBILE","EMAIL ADDRESS","COMPLETE ADDRESS","CITY","COUNTRY","BALANCE"))
                
                print("="*150) 
                
                for j in i:
                    print('%14s' % j,end=' ') 
                
                print()
                break
        else:
            print("!!.....RECORD NOT FOUND…..!!")
    except:
        print(".....NO SUCH TABLE EXISTS.....")
        
def Update():#Function to change the details of a customer
    try:	
        cmd="select * from BANK" 
        mycursor.execute(cmd) 
        S=mycursor.fetchall()
        A=input("Enter the account no whose details to be changed : ") 
        for i in S:
            i=list(i) 
            if i[0]==A:
                
                ch=input("Change Name(Y/N) :") 
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name :") 
                    i[1]=i[1].upper()
 

                ch=input("Change Mobile(Y/N) :") 
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Mobile :")

                ch=input("Change Email(Y/N) :") 
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter email :") 
                    i[3]=i[3].upper()

                ch=input("Change Address(Y/N) :") 
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address :") 
                    i[4]=i[4].upper()

                ch=input("Change city(Y/N) :") 
                if ch=='y' or ch=='Y':
                    i[5]=input("Enter City :") 
                    i[5]=i[5].upper()

                ch=input("Change Country(Y/N) :") 
                if ch=='y' or ch=='Y':
                    i[6]=input("Enter country :") 
                    i[6]=i[6].upper()

                ch=input("Change Balance(Y/N) :") 
                if ch=='y' or ch=='Y':
                    i[7]=float(input("Enter Balance :")) 
                    
                cmd="UPDATE BANK SET NAME=%s,MOBILE_NO=%s,EMAIL_ID=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s WHERE ACCNO=%s"
                    
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val) 
                mydb.commit() 
                    
                print("!!.....ACCOUNT UPDATED.....!!") 
                    
                break
        else:
            print("!!.....RECORD NOT FOUND…..!!")
    except:
        print(".....NO SUCH TABLE EXISTS.....")
       
def Delete():	#Function to delete the details of a customer
    try:
        cmd="select * from BANK" 
        
        mycursor.execute(cmd) 
        S=mycursor.fetchall()
        
        A=input("Enter the account no whose details are to be deleted : ") 
        p0 = int(input("Enter your password : "))
        print(p0)
        
        for i in S:
            
            i=list(i)
            
            if i[0]==A:
                
                cmd="delete from bank where accno=%s ; " 
                val=(i[0],)
                
                mycursor.execute(cmd,val) 
                mydb.commit() 
                
                print("!!.....ACCOUNT DELETED FROM RECORDS.....!!") 
                print("_____________________________________________________")
                print(" Your account ",A," has been deleted on your consent ")
                print("The money in the account is safe and can be taken out")
                print("easily with bank documents and proper id.            ")
                print("_____________________________________________________")
                
                break
 
        else:
            print("!!.....RECORD NOT FOUND…..!!")
    except:
        print(".....NO SUCH TABLE EXISTS.....")

def Debit(): #Function to Withdraw the amount by assuring the min balance of Rs 5000
    try:
        cmd="select * from BANK ;" 
        
        mycursor.execute(cmd) 
        S=mycursor.fetchall()
        
        print("Please Note that the money can only be debited if min balance of Rs 5000 exists")
        
        acc=input("Enter the account no from which the money is to be debited/withdrawn : ")
        p1 = int(input("Enter your password : "))
        print(p1)
        
        for i in S:
            
            i=list(i)
            
            if i[0]==acc:
                
                Amt=float(input("Enter the amount to be withdrawn : "))
                
                if i[7]-Amt>=5000:
                    
                    i[7]-=Amt
                    
                    b= i[7]
                    
                    cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s ;"
                    val=(i[7],i[0]) 
                    
                    mycursor.execute(cmd,val) 
                    mydb.commit() 
                    
                    print("___________________________________________")
                    print(".You have withdrawn Rs.",Amt,"            .")
                    print(".Your current balance is Rs.",b,".")
                    print("___________________________________________")
                    
                    break 
                else:
                    print("There must be min balance of Rs 5000") 
                    break

        else:
            print("!!.....RECORD NOT FOUND…..!!")


    except:
        print(".....NO SUCH TABLE EXISTS.....")

def Credit(): #Function to deposit an amount 
    try:
        cmd="select * from BANK;"
        
        mycursor.execute(cmd) 
        S=mycursor.fetchall()
        
        acc=input("Enter the account no to which the money is to be credited : ")
        p2 = int(input("Enter your password : "))
        print(p2)
        
        for i in S:
        
            i=list(i)
            
            if i[0]==acc:
            
                Amt=float(input("Enter the amount to be credited :"))
 
                i[7]+=Amt
                b =i[7]
                
                cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
                val=(i[7],i[0]) 
                
                mycursor.execute(cmd,val) 
                mydb.commit() 
                
                print("!!..... AMOUNT CREDITED.....!!") 
                print("__________________________________")
                print(".You have deposited Rs.",Amt)
                print(".Your current balance is Rs.",b,)
                print("__________________________________")
                
                break

        else:
            print("!!.....RECORD NOT FOUND…..!!")
 
    except:
        print(".....NO SUCH TABLE EXISTS.....")

def transfer_records():
    
    print("..... TRANSFER OF MONEY FROM ONE ACCOUNT TO OTHER WITHIN THE SAME BANK .....")
    try:
        cmd = "select * from BANK"
        
        mycursor.execute(cmd)
        S = mycursor.fetchall()
        
        acc1 = input("Please enter account no. from which money is to be transferred : ")
        acc2 = input("Please enter account no. to which money is to be transferred : ")
        
        if acc1 == acc2 :
                
                print()
                print("___________________________________________________________")
                print("! ! YOU CANNOT TRANSFER TO THE SAME ACCOUNT NUMBER ! !")
                print("___________________________________________________________")
                print()
                
                return transfer_records()
            
        for i in S:
            i = list(i)
            
            if (i[0] == acc1):
                
                Amt = float(input("Enter your desired amount to be transferred : "))
                i[7]-=Amt
                
                cmd = "UPDATE BANK SET BALANCE = %s WHERE ACCNO = %s"
                val = (i[7],i[0])
                
                mycursor.execute(cmd,val)
                mydb.commit()
                
                print("___________________________________________________________")
                print(". Amount of Rs.",Amt," has been deducted from your account.")
                print("___________________________________________________________")
                
                
        print("PLEASE NOTE THAT TRANSFER OF MONEY BETWEEN ACCOUNTS CAN HAPPEN")
        print("ONLY FOR THOSE ACCOUNTS WHICH HAVE RECORD IN OUR BANK")      
        
        print()
        
        print("TRANSFER BETWEEN DIFFERENT BANKS IS NOT FACILITATED")
        
        print()

        for i in S:
            i = list(i)
            
            if i[0] == acc2:
                i[7]+=Amt
                
                cmd = "UPDATE BANK SET BALANCE = %s WHERE ACCNO = %s"
                val = (i[7],i[0])
                
                mycursor.execute(cmd,val)
                mydb.commit()
                
                print("\n")
                
                print("_____________________________________________________________________________________")
                print(". Amount of Rs.",Amt," has been credited to your account number",acc1," from",acc2)
                print("_____________________________________________________________________________________")
                
                break
            
    
        else:
            print("Record not found")
            
    except:
        print("Table does not exist")
        
              
#FIXED_DEPOSIT - For the calculation of fixed_deposit of an amount
        
def Fixed_deposit_Create(): #Creates and checks the existence of table fixed_deposit
    
    try:
        mycursor.execute('create table FIXED_DEPOSIT(FD_ACCNO int(10),AADHAR_CARD_NO varchar(12),NAME varchar(20),PHONE_NO char(10),FD_AMOUNT float(10,3));')
        
        print("*TABLE CREATED*")
        
        Fixed_deposit_Create()
        
    except:
        print("*TABLE EXISTS*")
        
        Fixed_deposit()

        
def Fixed_deposit(): # Data insertion and caluclation of FD
    print("             $ $ $ $ $ FIXED DEPOSIT ACCOUNT CREATION $ $ $ $ $                ")
    
    while True:
        
        Acc1 = int(input("Enter FD_account no. : ")) 
        
        Aadhar_c=input("Enter Aadhar Card Number : ")
        
        Name1 = input("Enter Name : ")  
        
        Phone1 = input("Enter Phone_No. : ") 
        
        FdBal = float(input("Enter Fixed Deposit Amount : "))
        print()
        
        
        Rec = [Acc1,Aadhar_c,Name1.upper(),Phone1,FdBal]
        Cmd = "insert into FIXED_DEPOSIT values(%s,%s,%s,%s,%s)"
        
        mycursor.execute(Cmd,Rec)
        mydb.commit()

        cmd1 = "select * from FIXED_DEPOSIT "
        
        mycursor.execute(cmd1)
        a = mycursor.fetchall()
        
        print()
        print()
        
        
        print("..... FIXED DEPOSIT ACCOUNT CALCULATION .....")
        
        for i in a:
            i = list(i)
            
            if i[0] == Acc1:
                i[4]=FdBal
                
                cmd = "UPDATE FIXED_DEPOSIT SET FD_AMOUNT = %s WHERE FD_ACCNO = %s"
                val = (i[4],i[0])
                
                mycursor.execute(cmd,val)
                mydb.commit()
                
                print("Fixed deposit amount added")

        age = int(input("Enter your age : "))
        
        if age >=60:
            
            print("If age is greater than or equal to 60 then you will get 6.2 % rate")
            
            print("\n")      
                              
            print(".....CALCULATING AMOUNT AFTER MATURITY.....")
            
            a = FdBal
            t = float(input("Enter the number of years : "))
            r = 6.2
            
            maturity = a + a*((1 + r/100)**t)
            
            print("\n")
            
            print("Final Amount : {}".format(maturity))
            
        elif age < 60:

            print("If age is lesser than or equal to 60 then you will get 3% rate")
            
            print("\n")                        
             
            print(".....CALCULATING AMOUNT AFTER MATURITY.....")
            
            a1 = FdBal
            t1 = float(input("Enter the number of years : "))
            r1 = 3
            
            maturity = a1 + a1*((1 + r1/100)**t1)
            
            print("\n")
            
            print("Final Amount : {}".format(maturity))
            
            print("\n")

        else:
            print("!! INVALID CHOICE !!")
                    
        ch=input("Do you want to any other person as partner (y/n) : ")
        if ch == "y" or ch == "Y":
            Name2 = input("Please enter the name of the second holder : ")
            
            print("______________________________________________________________________")
            
            print("The account is secured with two holders")
            print(Name1)
            print(Name2)
            print(".....NOW,THE ACCOUNT CAN BE ACCESSED ONLY BY YOU AND YOUR PARTNER.....")
            
            print("______________________________________________________________________")
            print("..........THANK YOU..........")
            
            break
        
        if ch=='N' or ch=='n':
            
            print(".....THE ACCOUNT CAN BE ACCESSED ONLY BY YOU AND YOUR PARTNER.....")
            print("..........THANK YOU..........")

            break
        
# LOAN -  for the amount to be deposited after taking a loan
 
def Loan_Create(): #Creates and checks existence of loan
    try:
        mycursor.execute('CREATE TABLE LOAN(LOAN_ACCNO int(10),AADHAR_CARD_NO varchar(12),PANCARD_NO varchar(10),NAME varchar(20),PHONE_NO char(10),LOAN_AMOUNT int(10),TYPE_LOAN varchar(12));')
        
        print("*TABLE CREATED*")
        
        Loan_Create()
        
    except:
        
        print("*TABLE EXISTS*")
        
        Loan_Create()
        
        
def Homeloan():
    try:
            print("             $ $ $ $ $ LOAN ACCOUNT CREATION $ $ $ $ $                ")
    
            Acc2 = int(input("Enter Loan_account no. : ")) 
        
            Aadhar_c2=input("Enter Aadhar Card Number : ")
        
            Pan_card = input("Enter Pan Card number : ")
        
            Name2 = input("Enter Name : ")  
        
            Phone2 = input("Enter Phone_No. : ") 
        
            loan_type = input("Enter Loan type(home/personal) : ")
        
            Loan2 = float(input("Enter Loan Amount : "))
        
            print()
    
            Rec1 = [Acc2,Aadhar_c2,Pan_card,Name2.upper(),Phone2,Loan2,loan_type]
            Cmd1 = "insert into LOAN values(%s,%s,%s,%s,%s,%s,%s)"
        
            mycursor.execute(Cmd1,Rec1)
            mydb.commit()
            
            print("             $ $ $ $ $ LOAN CALCULATION $ $ $ $ $                ")
            print("\n")
                
            print("....................HOME LOAN....................")
                
            print("\n")

            salary = float(input('Please enter your annual salary: '))
                
            if salary in range(50000,100000):
                
                
                print("The bank will provide a loan in the range Rs. 2000 to Rs.80000")
                
                print("The interest rate will be 7% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 7
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)
                
                
            elif salary in range(100000,400000):
                
                
                print("The bank will provide a loan in the range Rs. 2000 to Rs.250000")
                
                print("The interest rate will be 7% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 7
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)

                
            elif salary in range(400000,1000000):
                
                
                print("The bank will provide a loan in the range Rs. 2000 to Rs.800000")
                
                print("The interest rate will be 7% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 7
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)

            
            elif salary in range(1000000,5000000):
                
            
                print("The bank will provide a loan in the range Rs. 2000 to Rs.4500000")
                
                print("The interest rate will be 7% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 7
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)

            
            
            elif salary in range(5000000,9000000):
                
            
                print("The bank will provide a loan in the range Rs. 2000 to Rs.8000000")
                
                print("The interest rate will be 7% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 7
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)
            
            
            elif salary in range(9000000,30000000):
                
                
                print("The bank will provide a loan in the range Rs. 2000 to Rs.25000000")
                
                print("The interest rate will be 7% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 7
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)
                
            else:
             
                print(".....INVALID.....PLEASE TRY AGAIN !!")
        
    except:
        
        print(".....NO SUCH TABLE EXISTS.....")  
        

def Personalloan():
    try:    
        print("             $ $ $ $ $ LOAN ACCOUNT CREATION $ $ $ $ $                ")
    
         
        Acc2 = int(input("Enter Loan_account no. : ")) 
        
        Aadhar_c2=input("Enter Aadhar Card Number : ")
        
        Pan_card = input("Enter Pan Card number : ")
        
        Name2 = input("Enter Name : ")  
        
        Phone2 = input("Enter Phone_No. : ") 
        
        loan_type = input("Enter Loan type(home/personal) : ")
        
        Loan2 = float(input("Enter Loan Amount : "))
        
        print()
    
        Rec1 = [Acc2,Aadhar_c2,Pan_card,Name2.upper(),Phone2,Loan2,loan_type]
        Cmd1 = "insert into LOAN values(%s,%s,%s,%s,%s,%s,%s)"
        
        mycursor.execute(Cmd1,Rec1)
        mydb.commit()
            
        print("....................PERSONAL LOAN....................")
            
        salary = float(input('Please enter your annual salary: '))
            
        if salary in range(50000,100000):
                
                print("The bank will provide a loan in the range Rs. 2000 to Rs.80000")
                
                print("The interest rate will be 11% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 11
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)

            
            
        elif salary in range(100000,400000):
                
                
                print("The bank will provide a loan in the range Rs. 2000 to Rs.250000")
                
                print("The interest rate will be 11% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 11
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)

        elif salary in range(400000,1000000):
            
                
                print("The bank will provide a loan in the range Rs. 2000 to Rs.800000")
                
                print("The interest rate will be 11% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 11
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)

            
        elif salary in range(1000000,5000000):
                
            
                print("The bank will provide a loan in the range Rs. 2000 to Rs.4500000")
                
                print("The interest rate will be 11% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 11
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)

                
        elif salary in range(5000000,9000000):
                
                
                print("The bank will provide a loan in the range Rs. 2000 to Rs.8000000")
                
                print("The interest rate will be 11% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 11
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)


        elif salary in range(9000000,30000000):
                
                
                print("The bank will provide a loan in the range Rs. 2000 to Rs.25000000")
                
                print("The interest rate will be 11% ")
                
                print("\n")
                
                years = int(input('Please enter number of years of loan: '))
                
                annual_r = 11
                
                Loan2 = float(input("Enter Loan Amount : "))
                
                r = (annual_r / 100) / 12  # decimal monthly interest rate from APR
                
                a = (r * Loan2 * ((1+r) ** years)) / (((1+r) ** years) - 1)
                
                print("\n")
                
                print('Monthly payment: ', a)

        else:
                
                print(".....INVALID.....PLEASE TRY AGAIN !!")
                
    except:
        
        print(".....NO SUCH TABLE EXISTS.....")   
        

# CONSUMER_DURABLE_LOAN - table to keep records for the customer who took loan for a product purchase
# created table CONSUMER_DURABLE_LOAN

def consumer_durable_loan():
    
    print("             $ $ $ $ $ CONSUMER DURABLE LOAN ACCOUNT CREATION $ $ $ $ $                ")
    
    while True:
        
        
        Acc3 = int(input("Enter Consumer_account no. : ")) 
        
        Aadhar_c3= int(input("Enter Aadhar Card Number : "))
        
        Product_name = input("Enter Product name from where the object is purchased : ")
        
        Shop_name = input("Enter Shop name from where the object is purchased : ")
        
        Moblie_no = int(input("Enter your mobile no. for OTP verification : "))
        
        Loan3 = float(input("Enter amount to be borrowed : ")) 
        
        print()


        Rec2 = [Acc3,Aadhar_c3,Product_name,Shop_name,Moblie_no,Loan3]
        Cmd2 = "insert into CONSUMER_D_LOAN values(%s,%s,%s,%s,%s,%s)"
        
        mycursor.execute(Cmd2,Rec2)
        mydb.commit()
        
        print("We offer consumer durable loans at 0%* interest and minimum payments.")
        print("We don’t ask for any security deposit on our Consumer Durable loans.")
        
        print("\n")
        
        print("             $ $ $ $ $ CONSUMER DURABLE LOAN ACCOUNT CALCULATION $ $ $ $ $                ")
        
        print("\n")


        p = Loan3 
        r = 0
        t = int(input("Enter number of months: " ))
        
        interest = (p * r * t)/100
        
        total = p + interest
        emi = total / t
        
        print("\n")
        
        
        print("Interest : ",interest)
        
        print("Monthly EMI = ", emi)
        
        print("\n")
        
        print("________________________________________________________________________________________")
        print(".Customer has to pay a monthly EMI of Rs.",emi," and has to pay an extra processing fee.")
        print("________________________________________________________________________________________")

        break

        
# Loop to run the whole program
while True:
    
    Menu()
    
    ch = input("Enter your choice : ")
    if ch == "1":            
            Create()
        
    elif ch == "2":
        while True:
            
            MenuSort()
            
            ch1 = input("Enter your choice a/b/c/d : ")
            if ch1 in ["a","A"]:
                
                DispSortAcc()
            elif ch1 in ["b","B"]:
                
                DispSortName()
            elif ch1 in ["c","C"]:
                
                DispSortBal()
            elif ch1 in ["d","D"]:
                print("Back to Main Menu")
                break
            else:
                print("Invalid Choice")
                
    elif ch == "3":
        
        DispSearchAcc()
        
    elif ch == "4":
        
        Update()
        
    elif ch == "5":
        
        Delete()
        
    elif ch == "6":
        
        while True:
            
            MenuTransaction()
            
            ch1 = input("Enter choice a/b/c/d : ")
            if ch1 in ["a","A"]:
                Debit()
                
            elif ch1 in ["b","B"]:
                Credit()
                
            elif ch1 in ["c","C"]:
                transfer_records()
                
            elif ch1 in ["d","D"]:
                print("Back to the main menu")
                break
            else:
                print("Invalid Choice")
                
    elif ch == "7":

            Fixed_deposit_Create()

    elif ch =="8":

        MenuLoan()
        
        ch1 = input("Enter your choice a/b/c : ")
        if ch1 in ["a","A"]:
                
                Homeloan()
                
        elif ch1 in ["b","B"]:
                Personalloan()
                
        elif ch1 in ["c","C"]:
                print("Back to the main menu")
                break
        else:
                print("Invalid Choice")
                        
    elif ch == "9":

            consumer_durable_loan()
        
    elif ch == "10":
        
        print("...EXITING...")
        print()
        print("Thank you for your interest,")
        print("If you are a resident of India accessing this website from within India,") 
        print("please contact Amit Kumar Singh at 022-3395 8000 or e-mail at sllipo@goldhorizonbank.com")
        print("for any other issues.")
        
        break
    
    else:
        
        print("_________________________________")
        print("X X WRONG CHOICE ENTERED X X")
        print("_________________________________")
    
