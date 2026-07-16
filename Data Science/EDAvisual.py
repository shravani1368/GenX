#setp 1 - Show first 5 elements
#step 2 - show dimentions data and its data type
#step 3 - show data statics
#step 4 - draw pie plot


import pandas as pd
import matplotlib.pyplot as plt
def main():
    df = pd.read_csv("./hello.csv")
    line  = "-"*64
    print(line)
    print("first 5 element")
    print(line)
    print(df.head())

    print(line)
    print("Dimensions")
    print(line)
    print(df.info())

    print(line)
    print("Statistics")
    print(line)
    print(df.describe(include="all",percentiles=[0.25,0.5,0.75]))

    dist_group = df.groupby("State Name")
    state_count = []
    state_name = []
    for i in dist_group:
        print(i[0],end=" ")
        print(len(i[1]))
        state_name.append(i[0])
        state_count.append(len(i[1]))  


#(n/total number)*100
#(num/779)*100
    state_count_percentage = []
    for num in state_count:
        s = (num/779)*100
        state_count_percentage.append(s)
    print(state_count_percentage)

    plt.figure(figsize=(10,10))
    plt.pie(state_count_percentage,labels=state_name,autopct="%0.1f%%")  #autopct means auto percentage text used to show the percentage in the pie chart 
    plt.show()

    plt.figure(figsize=(15,10))
    plt.bar(state_name,state_count_percentage)
    plt.xticks(rotation=90)
    plt.show()

# Draw a bar graph 
# x axis = state name and Y axis = average tem of that state 
df = pd.read_csv("./hello.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print(df.columns)  # check columns

avg_temp = df.groupby("State Name")["Average Summer Temperature"].mean()

# Clean column names
df.columns = df.columns.str.strip()

# Convert to numeric
df["Average Summer Temperature"] = pd.to_numeric(
    df["Average Summer Temperature"], errors='coerce'
)

# Group and calculate mean
avg_temp = df.groupby("State Name")["Average Summer Temperature"].mean()

print(avg_temp)

# Plot
states = avg_temp.index.tolist()
temps = avg_temp.values.tolist()

plt.figure(figsize=(15,10))
plt.bar(states, temps)
plt.xlabel("State Name")
plt.ylabel("Average Temperature")
plt.title("Average Temperature per State")
plt.xticks(rotation=90)
plt.show()
if __name__ == "__main__":
    main()


 