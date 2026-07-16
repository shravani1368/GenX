import joblib
def main():
    model = joblib.load("model.pkl")

    print(model.predict([[12,2]]))

if __name__ == "__main__":
    main()