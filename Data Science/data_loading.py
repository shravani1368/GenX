
import pandas

def main():
   
   data = pandas.read_csv("heightweight.csv")
   print(data)
   data = pandas.read_csv("heightweight.csv")
   avg = data["Height"].mean()
   print(avg)
   data["Height"] = data["Height"].fillna(avg)
   

   avg1 = data["Weight"].mean()
   print(avg1)
   data["Weight"] = data["Weight"].fillna(avg1)
   print(data)
   
if __name__ == "__main__":
    main()
