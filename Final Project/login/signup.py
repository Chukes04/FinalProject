def signup(): #signup to the website
    username = input("What would you like to be called")
    password = input("Make a strong password")
    with open("FinalProjectUsers.txt", "a") as f: #open the external fine
        f.write("\n")#start a new line
        f.writelines([username,", ", password])#append username and password to external file



def login(): #login to website
    with open('FinalProjectUsers.txt') as f: #open external file
        contents = f.read() #get the contents from file and store in variable
        escape = False
        while escape == False:
            username = input("enter username")
            password = input("enter password")
            if username and password in contents: #check if the inputed info is in file
                print ("You're in!")
                escape = True
            else:
                print ('Try again')

has_account = input("Do you have an account? Y or N").lower()
escape = False

while escape == False:
    if has_account == "y":
        login()
        escapse = True
        
    elif has_account == "n":
        signup()
        login()
        escapse = True
    else:
        print("Enter a valid input")
        has_account = input("Do you have an account? Y or N").lower
        escapse = True
    
