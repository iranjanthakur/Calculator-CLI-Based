def add(a, b):
  return a + b
  
def sub(a, b):
  return a-b
  
def mul(a, b):
  return a*b
  
def div(a, b):
  return a/b
  
while True:  
    print("\n" + "="*40)
    print ("Choose from 1 to 4 ")
    print("\n" + "="*40)
    print ("1. Add")
    print ("2. subtract")
    print ("3. Multiply")
    print ("4. Divide")
    print ("5. Exit")

    ranjan = int(input ("plsease select option between 1 to 4 :"))

    if ranjan == 5:
        print("\nThank you for using the calculator!")
        print("Goodbye! 👋")
        break

    a = int(input("Enter 1st number (only number) "))
    
    b = int(input("Enter 2nd number (only number) "))

    if ranjan == 1:
      print(a, "+" , b , "=" , add(a,b) )
  
    elif ranjan == 2:
      print(a, "-" , b , "=" , sub(a,b) )
  
    elif ranjan == 3 :
      print(a, "*" , b , "="  , mul(a,b))
  
    elif ranjan ==4  :
      print(a,  "/" ,b  ,  "="  ,  div(a,b))
  
    else :
      print("invalid input")
      print("\nThank you for using the calculator!")
      print("Goodbye! 👋")
   
