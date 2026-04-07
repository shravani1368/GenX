import multiprocessing
def add(a,b,q):
    result = (a+b)
    q.put(result)


def pow(a):
    num = a.get()
    print(num**2)

 

def main():
    q = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target = add,args=(10,11,q))
    p2 = multiprocessing.Process(target = pow,args=(q,))   
    p2.start()
    p1.start()
    p2.join # join is used to make the process to wait untill p1 get over
    


if __name__ == "__main__":
    main()


