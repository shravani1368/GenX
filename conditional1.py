import os

def main():
    name = input("Enter your name : ")
    gender = input("Enter your gender : ")
    

    if(gender =="male"):
        print("You are male")
        print(f"Hello {name} how are you?")
        os.system("say Hello")
    elif(gender =="female"):
        print(f"""You are female
        Hello {name}, how are you?""")
    else:
        print("Please enter valid input either male or female")

    
    
if (__name__== "__main__"):
    main() 