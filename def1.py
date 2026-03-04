def add(a,b):
     return(5+9)

def calculator(a,b):
    add=a+b
    sub=a-b
    prod=a*b
    div=a/b
    return ( add, sub, prod , div)

def origin():
    return(__name__)
o=origin()    
print(o)
def main():
    a,b,c,d= calculator(10,20)
    
    
    print(a)
    print(b)
    print(c)
    print(d)
    



if (__name__ == "__main__"):
    main()   