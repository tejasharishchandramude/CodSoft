import sys
print("===========================================")
print("\tCALCULATOR ")
print("===========================================")
print("\t1.Addition")
print("\t2.Subtraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Modulo Division")
print("\t6.Exponentiation")
print("\t7.Exit")
print("===========================================")
while(True):
    ch=int(input("Enter Your Choice :"))
    match(ch):
        case 1:
            val1=int(input("Enter First Value For Addition:"))
            val2=int(input("Enter Second Value For Addition :"))
            print("Addition ({} + {}) = {}".format(val1,val2,val1+val2))
        case 2:
            val1 = int(input("Enter First Value For Subtraction:"))
            val2 = int(input("Enter Second Value For Subtraction :"))
            print("Subtraction ({} - {}) = {}".format(val1, val2, val1 - val2))
        case 3:
            val1 = int(input("Enter First Value For Multiplication:"))
            val2 = int(input("Enter Second Value For Multiplication :"))
            print("Multiplication ({} * {}) = {}".format(val1, val2, val1 * val2))
        case 4:
            val1 = int(input("Enter First Value For Division:"))
            val2 = int(input("Enter Second Value For Division :"))
            print("Division ({} / {}) = {}".format(val1, val2, val1 / val2))
        case 5:
            val1 = int(input("Enter First Value For Modulo Division:"))
            val2 = int(input("Enter Second Value For Modulo Division :"))
            print("Modulo Division ({} // {}) = {}".format(val1, val2, val1 // val2))
        case 6:
            val1 = int(input("Enter Base Value:"))
            val2 = int(input("Enter Power :"))
            print("Exponentiation ({} ** {}) = {}".format(val1, val2, val1 ** val2))
        case 7:
            print("Thanks for using our Calculator")
            sys.exit()
        case _:
            print("Your choice of selection is wrong .... please try again")
    print("---------------------------------------------")
    print("Program execution completed ")
    print("---------------------------------------------")

