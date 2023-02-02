#Converts Farhenheit to celsius
#Request user input
#Process
#Deliver output
def Cel():
    Farhenheit= float(input("Enter: "))
    Celsius= float((9/5)* Farhenheit + 32)
    print ("The temperature is", Celsius,  "degrees celsius")
    
Cel()
#Converts Celsius to Farhenheit

def Far():
    Celsius=float(input("Enter:"))
    Farhenheit=(5*Celsius-160)
    Result =float(Farhenheit/9)
    print ("The temperature is",Result, "degrees Farhenheit")
    
  
Far()

