def main():
    
    n = int(input("Enter number: "))

    a, b = 0, 1
    count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1


if __name__ == "__main__":
    main()
