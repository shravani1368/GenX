def add(a,b,*args):
     print(a,b,args)
     c = a+b
     temp = 0
     for i in args:
         temp = temp+i
     return temp+c
def main():
     s= add(1,2,3,4,5)
     print(s)


if(__name__ == "__main__"):
    main()    