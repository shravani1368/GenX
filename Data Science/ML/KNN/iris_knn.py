import pandas as pd
import joblib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


def main():
    line = "-"*40
    
    df = pd.read_csv("iris.csv")
    
    print(df.head())
    print(line)
    print(df.info())
    print(line)
    print(df.describe())

    x = df[["sepal.length","sepal.width","petal.length","petal.width"]]
    y = df["variety"]

    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.4)

    model = KNeighborsClassifier(n_neighbors=50)
    model.fit(x_train,y_train)

    prediction = model.predict(x_test)

    for i,j in zip (prediction,y_test):
     print("prediction is: ",i)
     print("Actual answer is: ",j)

    Error = confusion_matrix(y_test,prediction) 
    print(Error)

    score = accuracy_score(y_test,prediction)
    print("score", score*100)

    joblib.dump(model,"iris_knn.pkl")




    


if __name__ == "__main__":
    main()
