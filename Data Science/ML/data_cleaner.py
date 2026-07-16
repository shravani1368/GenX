#step 1: Break the data in x and y 
#step 2: duplicate value remove
#step 3: find missing and fill them
#step 4: data Encoding
#step 5: feature scaling

import pandas as pd

def xy_splitter(dataset,target_varibale):
    X = dataset.drop(columns = target_varibale)
    y = dataset[target_varibale].column

    return X,y

def remove_duplicate():
    pass
def empty_value(X_columns):
    count = X_columns.isnull().count
    print(count)



def main():
    df = pd.read_csv("Salary_preediction2.csv")
    X,y = xy_splitter(df,"Monthly_Salary")

    df.isnull
    print(X)
    print(y)
    empty_value(X)


if __name__ == "__main__":
    main()
