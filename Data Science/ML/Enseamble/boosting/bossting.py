import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
def main():
     df = pd.read_csv("wineQT.csv")
     x = df.drop("quality", axis=1)
     y= df["quality"]
     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
     tree = DecisionTreeClassifier()
     model = AdaBoostClassifier(estimator= tree,n_estimators=60,learning_rate=0.1)
     model.fit(x_train,y_train)
     Y_pred = model.predict(x_test)
     score = accuracy_score(y_test,Y_pred)
     print("score",score*100)




if __name__ == "__main__":
    main()
