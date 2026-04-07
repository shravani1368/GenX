def countOfeven(list):
    a=0
    b=0
    for i in list:
        if(i%2 !=0):
            a=a+1
        else:
          b=b+1
    print("Number of elements which are odd",a)
    print("Number of element which are even",b)        


def main():
    list =[1,5,3,7,6,2,8]
    countOfeven(list)



if(__name__ == "__main__"):
    main()    