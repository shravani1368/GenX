
def main():
    name = input()
    print("Hello "+name)
    file = open("Greeting.txt","r")
    data = file.read()
    file.close()
    print(data)
if (__name__ == "__main__"):
    main()