import pandas as pd
def main():
    df = pd.read_csv("iris.csv")
   
    df = df.drop_duplicates()

    df.columns = df.columns.str.strip().str.lower()

    df[["sepal.length","sepal.width","petal.length"]].fillna(df[["sepal.length","sepal.width","petal.length"]].mean())

    df["variety"] = df["variety"].map({
        "setosa":0,
        "Versicolor":1,
        "Virginica":2
    })    

    x = df[["sepal.length","sepal.width","petal.length","variety"]]
    y = df["petal.width"]

    


      



if __name__ == "__main__":
    main()
