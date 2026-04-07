
def main():
     arr =[12,34,56,77,95,13]
     even = []
     odd = []
     for i in arr:
          if i%2 ==0:
           even = even+[i]
          else:
            odd = odd+[i] 
     print("Even numbers are: ",*even)
     print("Odd numbers are: ",*odd)
    
      
   



if __name__ == "__main__":
    main()
