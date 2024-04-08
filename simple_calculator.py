print("Welcome to Simple Calculator")
user = input("Enter operation (+ collection, - to subtract, * beaten, / for division) :\n")
if user not in ["+" ,"collection", "-", "subtract", "*", "beaten", "/", "division"] :
    print("Invalid choice ,Please run the program again and choose one of the available calculations")

if user in ["+" ,"collection", "-", "subtract", "*", "beaten", "/", "division"] :
   first_num = float(input("Enter first number :"))
   second_num = float(input("Elnter second number :"))
   if user == "collection" or user == "+" :
       print("Result :" ,first_num + second_num)
   elif user == "subtract" or user == "-" :
       print("Result :" ,first_num -second_num)
   elif user == "beaten" or user == "*" :
       print("Result :" ,first_num * second_num)
   elif user == "division" or user == "/" :
       print("Result :" ,first_num / second_num)
     
