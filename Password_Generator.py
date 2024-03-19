import random
while(True):
    try:

        print("-------------------------------------")
        length=int(input("Enter the length of the password :"))
        print("-------------------------------------")
        if (length)>75:
            print("Please enter the length of the password below 76")
        else:

            letters1="abcdefghijklmnopqrstuvwxyz"
            letters2="ABCDEFGHIJKLMNOPQRSTUVWXYX"
            numbers="0123456789"
            symbols="~!@#$%^&*_<>?"

            joiner=letters1+letters2+numbers+symbols

            password = "".join(random.sample(joiner, length))
            print("Your Password is : {}".format(password))
            print("-------------------------------------")
            a=input("Do you want to generate one more password(yes/no) :")
            if (a=="no"):
                print("Thanks for using our password generator")
                break
    except ValueError:
        print("Dont enter strs,special symbols for the length of the password ... try again")

