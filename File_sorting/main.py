from pathlib import Path
import schedule
import time

import os
FOLDER = "C:\\Users\\DELL\\Desktop"

PATH = os.path.join("")
print(PATH)

def file_sort():
    
    path = Path(FOLDER)

    for file in path.iterdir():

        ext = str(file).split(".")
        file_name=str(file).split("\\")

        if len(ext) > 1:
            if not os.path.exists(FOLDER+"\\"+ext[-1]):
                os.makedirs(FOLDER+"\\"+ext[-1])
                new_location = FOLDER + "\\" + ext[-1] + "\\" + file_name[-1]

                print("Old location : ",str(file))
                print("New Location : ",new_location)
                os.rename(str(file),new_location)

            else: 
                new_location = FOLDER + "\\" + ext[-1] + "\\" + file_name[-1]
                print("Old location : ",str(file))
                print("New Location : ",new_location+"\n")

                os.rename(str(file),new_location)

def main():

    schedule.every(1).minute.do(file_sort)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()