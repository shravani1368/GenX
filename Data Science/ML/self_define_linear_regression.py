# FORMULAE

# line of regression   :   y = mx + c
# m = sum((x-mean(x))(y-mean(y))) / (x-x_bar)**2
# c = mean(y) - m*mean(x)
import pandas as pd 
import numpy as np

def use(m,c,line):
    print(line)
    print("Ask price of bike enter CC ")
    a = int(input())

    print("Predicted Price is ; ",(m*a)+c)
    print(line)

def main():

    line = "-"*64

    df = pd.read_csv("./bike_price.csv")
    print("Bellow are first 5 entries of data")
    print(df.head())
    print(line)

    print("Below are dimentions of data")
    print(df.info())
    print(line)

    print("Bellow are stastics of data")
    print(df.describe())
    print(line)

    # -----------------------------------------------
    #       Linear Regression (Self - Define)
    # -----------------------------------------------
    
    # Seperates features and answers from data set
    feature = df["Bike_Power_CC"]
    answer = df["Bike_Price_INR"]

    # Split Into Training and Testing of data set
    # Training
    x_train = []
    y_train = []

    for data in range(0,6) :
        x_train.append(feature[data])
        y_train.append(answer[data])
    
    # Testing
    x_test = []
    y_test = []
    for data in range(6,10):
        y_test.append(answer[data])
        x_test.append(feature[data])

    print(line)
    print("These are Features of Training : ",x_train)
    print("These are Y for Training : ",y_train)
    print(line)
    print(line)
    print("These are Features of Testing : ",x_test)
    print("These are Y for Testing : ",y_test)
    print(line)

    x_ = np.mean(x_train)
    print("Mean of Training features(X) : ",x_)

    y_ = np.mean(y_train)
    print("Mean of Training Y : ",y_)

    print(line)

    # x - mean(x)
    # y - mean(y)
    x_sub_xBar = []
    y_sub_yBar = []
    for data in range(0,6):
        x_sub_xBar.append(x_train[data]-x_)
        y_sub_yBar.append(y_train[data]-y_)

    print(line)
    print("x-mean(x) : ",x_sub_xBar)
    print("y-mean(y)",y_sub_yBar)
    print(line)

    # (x - mean(x)) * (y - mean(y))
    x_sub_xBar_y_sub_yBar = []

    for data in range(0,6):
        x_sub_xBar_y_sub_yBar.append(x_sub_xBar[data] * y_sub_yBar[data])
        
    print(line)
    print("(x - mean(x)) * (y - mean(y)) : ",x_sub_xBar_y_sub_yBar)
    print(line)

    # (x  - mean(x))^2
    x_sub_xBar2 = []
    for data in range(0,6):
        x_sub_xBar2.append(x_sub_xBar[data]**2)

    print(line)
    print("(x - mean(x))^2 : ",x_sub_xBar2)
    print(line)

    sum_x_sub_xBar_y_sub_yBar = 0
    sum_x_sub_xBar2 = 0
    for data in range(0,6):
        sum_x_sub_xBar2 += x_sub_xBar2[data]
        sum_x_sub_xBar_y_sub_yBar += x_sub_xBar_y_sub_yBar[data]

    # Calculating M and C
    m = sum_x_sub_xBar_y_sub_yBar/sum_x_sub_xBar2
    c = y_ - (m*x_)
    print(line)
    print("Value of M : ",m)
    print("Value of C : ",c)
    print(line)


    # Testing

    err = 0
    for data in range(0,4):
        y_hat = (m*(x_test[data])) + c 
        errr = y_test[data] - y_hat
        err += errr

    error = err/4
    print(line)
    print("Error is ",error)
    print(line)

    print("\n\n",line)
    print("MODEL IS TRAIN")
    print(line,"\n\n")

    use(m,c,line)


if __name__ == "__main__":
    main()
