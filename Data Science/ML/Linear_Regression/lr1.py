import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def main():
    df = pd.read_csv("salary_pred.csv")
    print(df.head())

    print("Dimentions of Data set")
    print(df.info())

    print("Stat of Data set")
    print(df.describe())

    df["EducationLevel"] = df["EducationLevel"].map({
        "Bachelors" : 0,
        "Masters" : 1,
        "PhD" : 2
    })

    print(df.head())
    
    x = df[["YearsExperience","EducationLevel"]]
    y = df["Salary"]

    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=42)

    model = LinearRegression()
    model.fit(x_train,y_train)

    Y_pred = model.predict(x_test)

    for i,j in zip(y_test,Y_pred):
        print(f"Actual value : {i} Predicted Value : {j}")

    error = mean_absolute_error(y_test, Y_pred)
    print(error)

if __name__ == "__main__":
    main()