import datetime
from multiprocessing import Process
def process1():
    print("p1: Hello World")
    for i  in range(1,1000001):
        pass

def process2():
    value = 1
    for i in range(1,50):
        value= i*value

def main():
    start_time = datetime.datetime.now()
    print("Executing p1 & p2")
    p1 = Process(target = process1)
    p2 = Process(target = process2)

    p1.start()
    p2.start()
    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    print(total_time)


if __name__ == "__main__":
    main()   