import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score 
def main():
     df = pd.read_csv("iris.csv")
     x = df.drop("variety", axis=1)
     y= df["variety"]
     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
     model1 = KNeighborsClassifier(n_neighbors=15)
     model2 = DecisionTreeClassifier(max_depth=4)
     model3 = SVC()
     model1.fit(x_train,y_train)
     Y_pred = model1.predict(x_test)
     score = accuracy_score(y_test,Y_pred)
     print("score of model1 ", score*100)

     model2.fit(x_train,y_train)
     Y_pred = model2.predict(x_test)
     score = accuracy_score(y_test,Y_pred)
     print("score of model2 ", score*100)
     
     model3.fit(x_train,y_train)
     Y_pred = model3.predict(x_test)
     score = accuracy_score(y_test,Y_pred)
     print("score of model3 ", score*100)



if __name__ == "__main__":
    main()
