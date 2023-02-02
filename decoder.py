#import string
#define function(main)
#Request input
#loop through input and split input with a condition " " or ","
#revert input to integer ussing eval
#convert evaluated data to text using char attribute.
import string
def main():
    message = input("Enter message to decode:")
    for mess in str.split(message, ","):
        result=eval(mess)
        output = chr(result)
        print (output)
        
main()





