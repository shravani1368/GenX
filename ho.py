def cal(a):
    return a(10,11)
def add(a,b):
    return a+b
def main():
    s = cal(add)
    print(s)



if(__name__ == "__main__"):
    main()   