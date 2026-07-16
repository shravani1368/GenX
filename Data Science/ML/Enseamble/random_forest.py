import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest,f_classif
import utils
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score

def data_cleaning(df):
    f_num = df.select_dtypes(include = "number").columns
    for col in f_num:
        df[col] = df[col].fillna(df[col].mean())
    df = df.drop_duplicates()
    return df

def preprocessing(df,prediction_column):
    x= df.drop(df[[prediction_column]],axis=1)  
    y=df[prediction_column]  
    x,y = utils.clean_outliers(x,y)
    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2)
    return x_train,x_test,y_train,y_test 

def feature_selection(x_train,y_train):
    selector = SelectKBest(score_func=f_classif, k=5)
    x_new = selector.fit_transform(x_train,y_train)
    return x_new

def train(x_train,y_train):
    model = RandomForestClassifier(n_estimators=101,max_depth=11) # parameter tuning
    model.fit(x_train,y_train)
    return model

def model_evalution(x_test,y_test,model):
    Y_pred = model.predict(x_test)
    Error = confusion_matrix(y_test,Y_pred) 
    print(Error)

    score = accuracy_score(y_test,Y_pred)
    print("score", score*100)
    return Error,score

def main():
    df =  pd.read_csv("WineQT.csv")
    df1 = data_cleaning(df)
    X_train, X_test, y_train, y_test = preprocessing(df1,"quality")
    x_new= feature_selection(X_train,y_train)
    model = train(X_train,y_train)
   
    Error,score= model_evalution(X_test,y_test,model)

    
    


if __name__ == "__main__":
    main()

