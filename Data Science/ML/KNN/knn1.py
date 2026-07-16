import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

def main():
    line = "-"*40
    
    df = pd.read_csv("Dog_cat.csv")
    
    print(df.head())
    print(line)
    print(df.info())
    print(line)
    print(df.describe())

    x = df[["Height_cm","Weight_kg"]]
    y = df["Label"]

    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train,y_train)

    prediction = model.predict(x_test)

    for i,j in zip (prediction,y_test):
     print("prediction is: ",i)
     print("Actual answer is: ",j)

    Error = confusion_matrix(y_test,prediction) 
    print(Error)




    


if __name__ == "__main__":
    main()
