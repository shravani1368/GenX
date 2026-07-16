#IQR = Q3 - Q1
#lower bound = Q1 - 1.5*IQR
#upper bound = Q3 + 1.5*IQR

import pandas as pd

def IQR(df):
    Q1 = df.quantile(0.25)
    Q2 = df.quantile(0.50)
    Q3 = df.quantile(0.75)

    IQR = Q3 - Q1

    lb = Q1- 1.5*IQR
    up = Q3+ 1.5*IQR
    outliars = [(df>up) & (df<lb)]# here the df data is from pandas and it is in C language that's why we used the

    return outliars

def main():

    df = pd.read_csv("Mango_weight.csv")
    x=df.drop(["Mango_ID","Status"],axis=1)  #default 0 = y axis and 1 = x axis
    y=df["Status"]

    print(IQR(x))


if __name__ == "__main__":
    main()