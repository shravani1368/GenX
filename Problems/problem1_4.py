def main():
    i = 0
    while(i<=10):
        
        i+=1
    list = [] 
    init = True
    print("For stoping enter stop")
    while(init):
        k = input(" ")
        if(k!= "stop"):
         k=int(k)
         list.append(k)
        else:
           init = False 
    print(list)
    


if(__name__ == "__main__"):
    main()        




