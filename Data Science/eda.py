#Exploratary Data Analysis
#Step 1 -Load data set
#step 2 - show first 5 Enteries of data
#step 3 - show Dimensions of data set
#step 4 - show the statistics of data set
#step 5 - split data into dependent and independent data

import pandas as pd 
def main():
    line = "-"*64
    df = pd.read_csv("./salary.csv")  #df - data frame
    print(line)
    print("FIRST FIVE ENTRIES")
    print(line)
    print(df.head())  #head will print first 5 elements
    print(line)
    print("DATA SET INFO")
    print(line)
    print(df.size)    # size variable will multiply the number of rows and columns 
    print(df.info())  #dimenstion of the data set 
    print(line)
    print("DATA SET STATISTICS")
    print(line)
    print(df.describe())

    featuers = [
        df["Experience"], 
        df["Education_Level"],
        df["Age"]]
    
    answer = df["Salary"]
    print(answer)
if __name__ == "__main__":
    main()
