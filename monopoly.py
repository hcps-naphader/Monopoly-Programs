import os
def monopoly():
  try:
    os.system("clear")
    print("MONOPOLY MONEY COUNTER \n")
    fh = int(input("How many $500 bills do you have?\n"))
    a = 500*fh
    os.system("clear")
    print("MONOPOLY MONEY COUNTER \n")
    h = int(input("How many $100 bills do you have?\n"))
    b = 100*h
    os.system("clear")
    print("MONOPOLY MONEY COUNTER \n")
    f = int(input("How many $50 bills do you have?\n"))
    c = 50*f
    os.system("clear")
    print("MONOPOLY MONEY COUNTER \n")
    t = int(input("How many $20 bills do you have?\n"))
    d = 20*t
    os.system("clear")
    print("MONOPOLY MONEY COUNTER \n")
    ten = int(input("How many $10 bills do you have?\n"))
    e = 10*ten
    os.system("clear")
    print("MONOPOLY MONEY COUNTER \n")
    five = int(input("How many $5 bills do you have?\n"))
    f = 5*five
    os.system("clear")
    print("MONOPOLY MONEY COUNTER \n")
    one = int(input("How many $1 bills do you have\n"))
    g = 1*one
    os.system("clear")
    total = (a + b + c + d + e + f + g)
    print("MONOPOLY MONEY COUNTER")
    print("\nYou have a total of " + "$" + str(total) + " dollars!")
    cont = input("\nWould you like to Count Money(1),Do Tax(2),or Exit(3) 1|2|3\n")
    if cont == "1":
      monopoly()
    elif cont == "2":
      os.system("clear")
      td = total * .10
      x = round(td, 0)
      print("You have a total of " + "$" + str(total) + " dollars!")
      print("\nYour tax you have to pay is " + "$" + str(x))
      cont2 = input("\nWould you like to count money again(1) or exit?(2)\n")
      if cont2 == "1":
        monopoly()
      elif cont2 == "2":
        exit()      
    elif cont== "3":
      exit()
  except(Exception):
    error = input("\nYou have done an error! Type the letter 'y' to continue!\n")
    if error == "y":
      monopoly()
    else:
      exit()
monopoly()
