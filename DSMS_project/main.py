import sys
import os
#This creates new file ->none
#Date 15-03-26
def create_table(cmd_list:list):

    if cmd_list[1] == "INTO":
      file = open("./" +cmd_list[3]+"/Untitled.csv","w")
      file.close()
    else:
       file_name = cmd_list[1]
       file = open("./" +cmd_list[3]+file_name+".csv","w")
       file.close()
      

# This is root (entry point function ) -> none
# Date - 15-03-26
def main():
    if len(sys.argv)>= 2:
        if sys.argv[1] == "--h":
            print('''
            to create a new DB : CREATE_DB <database_name>
            to create a table  : CREATE_TABLE <table_name> INTO <db_name>
        ''')
        
    terminate = False
    while terminate == False:

        cmd = input()
        splited_cmd = cmd.split(" ")
        if cmd == exit:
            break

        if splited_cmd[0] == "CREATE_DB":

           if len(splited_cmd) <2:
            db_name = "Untitled"
           else:
            db_name = splited_cmd[1] 

            os.makedirs("./root/" +db_name)
        elif splited_cmd[0] == "CREATE_TABLE":
           create_table(splited_cmd)
           
    



if(__name__ == "__main__"):
    main()    