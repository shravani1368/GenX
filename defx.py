def add(no1, no2):
     return no1+no2
def sub(no1 ,no2):
     return no1- no2
def div(no1, no2):
     return no1/no2
def mod(no1,no2):
     return no1%no2
def prod(no1,no2):
     return no1*no2
def main():
     a = 10
     b = 8
     add = add(a,b)
     sub = sub(a,b)
     div = div(a,b)
     mod = mod(a%b)
     prod = prod(a*b)
     print(add)
     print(sub)
     print(div)
     print(prod)
     print(mod)

if (__name__ == "__main__"):
    main()   