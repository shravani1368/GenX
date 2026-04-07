def iseven(list):
    a = 0
    b = 0

    for i in list:
        if(i%2 ==0):
            a=a+1
        
        else:
            b=b+1
    print(a,b)
def main():
    list = [1,2,3,4,5]
    iseven(list)   

if(__name__ == "__main__"):
    main()             
        
        


