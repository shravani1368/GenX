def main():
  que_set1={
     "who is national animal":["kutra","Manjar","Popat","Tiger",3],
     "which is national anthum":["Sukh karta","hanuman chalisa","jana gana mana","nacho nacho",2],
     "national flower ?":["rose","lotus","lilly","hisbiscus",1],
     "native language of maharashtra ? ":["hindi","marathi","sanskrit","urdu",1],
     "fingers in one hand":["1","4","5","8",2]
  }

  que_set2={
     "which is the primary colour":["Purple","Indigo","Baby pink","Red",3],
     "which number is odd ":["10","11","8","4",1],
     "Which is favourite folwer of loard Ganesh":["rose","lotus","lilly","hisbiscus",3],
     "Pune's famous dish":["Misal pav","Idli","Samosa","Dosa",0],
     "India's national Game":["Basketball","Hockey","Cricket","Table tennis",2]
  }
  que_set3={
     
     "Which language is popular for AI?":["HTML","CSS","Python","SQL",2],
     "What we call rows in SQL":["Attribute","Tuple","row","relation",1],
     "Which device process data":["CPU","Keyboard","Mouse","Monitor",0],
     "What stores data permanently":["ROM","RAM","Cahe","Regiter",0],
     "Which software detect virus?":["OS","Antivirus","Compiler","Browser",1]
  }

  que_set4={
     "who is used to secure communication":["Execution","Decryption","Encryption","Compilation",2],
     "which memory is volatile ":["ROM","RAM","HDD","SSD",1],
     "Whic is storage device ":["HardDisk","Keyboard","CPU","Mouse",0],
     "Which protocol is used for webpages":["HTTPS","FTP","SMTP","TCP",0],
     "Which network cover large area":["LAN","WAN","MAN","PAN",1]
  }

  question_sets=[que_set1,que_set2,que_set3,que_set4]
  terminator=True

  print("Message : for more detail type help")
  option=1
  while(terminator):
     cmd=input(">>>")
     if cmd=="exit":
        exit()
     elif cmd=="help":
        print(""" 
                To start the game say "start"
                if yo want to exit say "exit"
                if you want to choose different topic say "options"
                to add your own quiz for quiz just say "add-quiz"
              """)
        
     elif cmd=="options":
        print(""" 
                type 1 for :  MYTHOLOGY
                type 2 for :  GK
                type 3 for :  HISTORY
                type 4 for :  COMPUTER
              """)
        option=int(input(">>>")) 
     elif cmd=="start":
        point=0
        for questions in question_sets[option]:
          print(questions+"\n")

          for ops in range(0,len(question_sets[option][questions])-1): # OR range(0,4)
            print("\t",ops+1,question_sets[option][questions][ops]) 

         # ans=int(input())-1
          ans=input()   

          if ans.isdigit():
             ans= int(ans)-1
          elif ans=="exit":
             print(f"You scored {point}/5") 
             exit()

          if question_sets[option][questions][-1]==ans:
               point+=1
        print(f"You scored {point}/5") 

     elif cmd=="add-quiz":
        quiz={}
          
        print("Enter your Quiz Title")
        title=input()

        for question in range(1,5):
           print(f"Enter questions no {question}")
           key=input()
           options=[]

           for val in range(1,5):
              if val==5:
                value=int(input("Enter answer of this question ") ) 
              else:
                 value=input(f"Enter option {val} :")
           
              options.append(value)

           quiz[key]=options
        print(quiz)
        question_sets.append(quiz)
        options=-1
        print(question_sets)
if __name__ == "__main__":
    main()