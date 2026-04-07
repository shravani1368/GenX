import datetime
def process1():
    print("p1: Hello World")
    for i  in range(1,1000001):
        pass
    
def process2():
    value = 1
    for i in range(1,1001):
        value = i*value

def main():
    start_time = datetime.datetime.now()
    process1()
    process2()
    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    print(total_time)



if __name__ == "__main__":
    main()   