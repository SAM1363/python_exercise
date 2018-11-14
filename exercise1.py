# input();
# name = input
# print(name)
# # int(string)
# age = int(input("what is your age"))

# print(name)

# print (age + 7)

# age = 19
# if age >= 21:
#     print("you can drink")
# elif age < 18:
#     print("what are you doing here")    
# else :
#     print("you live somewhere...")

# 

# answer = ""

# while answer != "when":
#     answer = input("say when: ")
#     answer = answer.lower()

# print("say cheese")    


# name = input("Enter your name:")
# print("Hello, " + name)

# name = input("ENTER YOUR NAME:")
# print("Hello, " + name.upper())
# print("YOUR NAME HAS " + str(len(name))  + " LETTERS IN IT")
# print("Please fill in the blanks below:")
# print("____(name)____'s favorite subject in school is ____(subject)____. ")
# name = input("What is name?: ")
# subject = input("What is subject?: ")
# print(name + "`s favorite subject in school is " + subject)


# day = int(input('Day (0-6)? ')) 
# if (day == 0):
#     print("Sunday")
# elif (day == 1):
#     print("Monday") 
# elif (day == 2):
#     print("Tuesday") 
# elif (day == 3):
#     print("Wednesday")
# elif (day == 4):
#     print("Thursday")   
# elif (day == 5):
#     print("Friday")   
# else:
#     print("Saturday")   

# day = int(input('Day (0-6)? ')) 
# if (day == 0):
#     print("Go to work")
# elif (day == 1):
#     print("Seelp in") 
# elif (day == 2):
#     print("Seelp in") 
# elif (day == 3):
#     print("Seelp in")
# elif (day == 4):
#     print("Seelp in")   
# elif (day == 5):
#     print("Seelp in")   
# else:
#     print("Go to work")   

# Celsius = int(input("Temperatue in C?: "))
# Fahrenheit = (Celsius * 1.8 ) + 32
# print(Fahrenheit , "F")


# TotalBill = int(input("Total bill amount? "))
# Servicelevel = (input("Level of service? "))
# if (Servicelevel == "good"):
#     tip = TotalBill * 0.2   
# elif (Servicelevel == "fair"):
#     tip = TotalBill * 0.15
# elif (Servicelevel == "bad"):
#     tip = TotalBill * 0.10  
# TotalAmount = TotalBill + tip
# print("TotalTip:  ${:.2f}".format(tip))

# print("TotalAmount: ${:.2f}".format(TotalAmount))



# TotalBill = int(input("Total bill amount? "))
# Servicelevel = (input("Level of service? "))
# Split = int(input("How many ways? "))
# if (Servicelevel == "good"):
#     tip = TotalBill * 0.2   
# elif (Servicelevel == "fair"):
#     tip = TotalBill * 0.15
# elif (Servicelevel == "bad"):
#     tip = TotalBill * 0.10  
# TotalAmount = TotalBill + tip
# PerPerson = TotalAmount / Split
# print("TotalTip:  ${:.2f}".format(tip))
# print("TotalAmount: ${:.2f}".format(TotalAmount))
# print("PerPerson: ${:.2f}".format(PerPerson))


# count = 0
# while count < 10:
#     count += 1
#     print(count)


coin = 0
x = "yes"
while x == "yes":
    print("You have " + str(coin) + " coins.")
    coin += 1
    x = input("Do you want another? ")
print("Bye")

