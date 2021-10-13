
import sys


def Passwords():
    first_name = input("Please enter your First Name: ")
    last_name = input("Please enter your Last Name: ")
    your_email = input("Please enter your Email Address: ")
    

    detail_ = first_name + last_name

    detail_nospace = detail_.replace(" ", "")
    
    details = detail_nospace + your_email
    list(details)
    password = details[2] + details[0] + details[-1] + details[4] + details[8] + details[6] + details[2]
    print("Your Password is " + password)

    
    response = int(input("To change this password, Enter 1 to save this password to our database, Enter 2: "))

    try:
        if response == 1:
            new_password = input("Please enter your desired password: ")
            print("Your password is: " + new_password)
            d = open('user.txt', 'w')
            d.write(first_name)
            d.write(" ")
            d.write(last_name)
            d.write(" ")
            d.write(your_email)
            d.write(" ")
            d.write(new_password)
            d.close()


        else:
            d = open('user.txt', 'w')
          
            d.write(first_name)
            d.write(" ")
            d.write(last_name)
            d.write(" ")
            d.write(your_email)
            d.write(" ")
            d.write(password)
            d.close()

        
            sys.exit()
    except ValueError:
        print("Invalid response")
        sys.exit()

Passwords()
