def main():
    arr =[10,20,30,5]
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    print("Smallest number in array is :",smallest)        



if __name__ == "__main__":
    main()
