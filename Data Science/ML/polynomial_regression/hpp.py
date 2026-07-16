import Foundation as fd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
def main():
    df = fd.Data_loading("house.csv","csv")

    print( fd.Analysis(df))

    df= fd.Clean_data(df)
    x = df.drop("Price_USD", axis=1)
    y = df["Price_USD"]
    
    poly = PolynomialFeatures(degree=2)
    x= poly.fit_transform(x)

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
    model = fd.regression(x_train,y_train)
    Accuracy = fd.evalution(x_test,y_test,model)
    print(Accuracy*100)
    

    








if __name__ == "__main__":
    main()
