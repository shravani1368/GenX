import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def main():
    line = "-"*65
    df = pd.read_csv("Dog_cat.csv")
    print(df.head())
    print(line)
    print(df.info())
    print(line)
    print(df.describe())

    x = [["Height_cm","Weight_kg"]]
    y = ["Label"]

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

    model= KNeighborsClassifier(n_neighbors= 8)
    model.fit(x_train,y_train)

    prediction = model.predict(x_test)

    for i,j in zip(prediction,y_test):
        print("predicition is",i)
        print("actual value is ",j)
    
    


if __name__ == "__main__":
    main()
