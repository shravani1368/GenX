
def main():
    name = input("Enter your name : ")
    gender = input("Enter your gender : ")
    

    if(gender =="male"):
        print("You are male")
        print("Hello",name,"how are you?")
        
    elif(gender =="female"):
        print("You are female")
        print("Hello",name,"how are you?")
    else:
        print("Please enter valid input either male or female")
if (__name__ == "__main__"):  
       main()
    
