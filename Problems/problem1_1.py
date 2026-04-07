def iseven(list):
    for i in list:
        if(i&1):
         print("1")
        else:
           print("0") 
    
def main():
    list = [2,3,4,5]
    iseven(list)
if(__name__ == "__main__"):
   main()    