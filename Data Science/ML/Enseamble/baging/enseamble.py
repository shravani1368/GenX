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
    
    knn=  KNeighborsClassifier(n_neighbors=15)
    decision_tree = DecisionTreeClassifier(max_depth=4)
    svm = SVC()
    model = VotingClassifier(
        estimators=[
            ("knn",knn),
            ("svm",svm),
            ("Decisiontree",decision_tree)
        ],
        voting = "hard"  #soft
    )
    model.fit(x_train,y_train)
    Y_pred = model.predict(x_test)
    score = accuracy_score(y_test,Y_pred)
    print("score", score*100)
    print(model.named_estimators_.items())


    
    


if __name__ == "__main__":
    main()
