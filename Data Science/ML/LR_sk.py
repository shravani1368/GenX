#Linear Regression scikitlearn

import pandas as pd
from sklearn.model_selection import train_test_split

#from sklearn  library model_selection module import train_test_split function /class
from sklearn.linear_model  import LinearRegression
from sklearn.metrics import mean_squared_error
#mean sq error gives error 

def main():
    #Step 1:- load data set
    df=pd.read_csv("multi_feature.csv")

    #Step 2:- Split into dependant and indepandant
    x=df[["x1","x2"]]
    y=df["ans"]

    #Step 3:- Split into training and testing data set
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)
    #train_test_split  splits data as well as shuffels it so that data has varity in training and testing 
    # train_test_split asks for 2d array thus two [[]] in x
    print("X for training ",x_train)
    print("X for testing ",x_test)
    print("Y for training ",y_train)
    print("Y for testing ",y_test)

    #Step 4:- train your model
    model=LinearRegression()
    model.fit(x_train,y_train) # fit used to tells the model to use this data 

    #Step 5 :- predict 
    y_pred=model.predict(x_test)

    #Compare actual and predicted values
    print("Actual ans : ",y_test)
    print("Predicted ans: ",y_pred)

    # find error
    MSE=mean_squared_error(y_test,y_pred)
    print("The error is :",MSE)

if __name__ == "__main__":
    main()