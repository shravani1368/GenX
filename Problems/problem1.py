
def iseven(list):
    
    for i in list: 
     if(i%2 != 0):
        print("All are odd")
     else:
       print(" All are even")
def main():
     list = [2,4,6,8]
     iseven(list)
    
if(__name__ == "__main__"):
    main()    