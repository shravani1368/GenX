import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest,f_classif
import utils
import joblib




def data_cleaning(df):
    f_num = df.select_dtypes(include="number").columns
    for col in f_num:
        df[col] = df[col].fillna(df[col].mean())
    df = df.drop_duplicates()
    
    return df

def preprocessing(df,prediction_column):
    # X and Y splitting
    # X = [["PassengerId","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]]
    # y = ["Survived"]
    X = df.drop(df[[prediction_column]],axis=1)
    y = df[prediction_column]
    x,y = utils.clean_outliers(x,y)
    # Data splitting 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    
    return X_train, X_test, y_train, y_test

def train(X_train,y_train):
    model = tree.DecisionTreeClassifier(max_depth=4)
    model.fit(X_train,y_train)
    return model

def evalution(model,X_test,y_test):
    Y_pred = model.predict(X_test)
     
    Error = confusion_matrix(y_test,Y_pred) 
    print(Error)

    score = accuracy_score(y_test,Y_pred)
    print("score", score*100)
    return Error,score

def feature_selection(X_train,y_train):
            
    selector = SelectKBest(score_func=f_classif, k=5)
    X_new = selector.fit_transform(X_train, y_train)
    
    return X_new





def main():
    df =  pd.read_csv("WineQT.csv")
  

    s = data_cleaning(df)
    X_train, X_test, y_train, y_test = preprocessing(s,"quality")
    model = train(X_train,y_train)
    Error,score= evalution(model,X_test,y_test)
    plt.figure(figsize=(12,8))
    X_new = feature_selection(X_train,y_train)
    tree.plot_tree(model)
    plt.show()
    


    joblib.dump(model,"model.pkl")

if __name__ == "__main__":
    main()
