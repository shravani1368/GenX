def main():
    print("Enter the number")
    num = int (input())
    num = abs(num)
    count = 0
    if num == 0:
        count = 1
    else:    
        while num>0:
            num = num
            count+=1
    print("count of digits",count)
        
       


if __name__ == "__main__":
    main()
