def main():
    arr = [1,6,4,8,3]
    greatest = arr[0]
    for i in arr:
        if i > greatest:
            greatest = i
    print("Greatest Number in Array is : ",greatest)
        

if __name__ == "__main__":
    main()
