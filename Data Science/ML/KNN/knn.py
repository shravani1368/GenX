import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
def main():
    line = "-"*40
    
    df = pd.read_csv("Dog_cat.csv")
    
    print(df.head())
    print(line)
    print(df.info())
    print(line)
    print(df.describe())

    x = df[["Height_cm","Weight_kg"]]
    y = df["Label"]

    model = KNeighborsClassifier(n_neighbors=15)
    model.fit(x,y)

    Prediction = model.predict([[40,50]])
    print(Prediction)


    


if __name__ == "__main__":
    main()
