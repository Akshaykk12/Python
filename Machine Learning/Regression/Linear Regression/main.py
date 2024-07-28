import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./Update.csv")
# print(data)                                                                   #To see the data

# print(data.columns)                                                           #To see the names of the columns
data.columns = data.columns.str.strip()                                         #To remove all the empty spaces in the column name
# print(data.columns)

if data.isna().sum().sum() > 0:                                                 #Remove all the nan values in the data
    print("Data contains NaN values. Dropping NaNs.")
    data = data.dropna()

data["OPEN"] = data["OPEN"].str.replace(',','').astype(float)                   #Remove all the commas in the data and convert it to float
data["HIGH"] = data["HIGH"].str.replace(',','').astype(float)

data['OPEN'] = (data['OPEN'] - data['OPEN'].mean()) / data['OPEN'].std()        #Normalize the data
data['HIGH'] = (data['HIGH'] - data['HIGH'].mean()) / data['HIGH'].std()

# plt.scatter(data['OPEN'], data['HIGH'])                                       #Visualize the data
# plt.show()


def loss_function(m, b, points):                        
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].OPEN
        y = points.iloc[i].HIGH 
        total_error += (y - (m * x + b)) ** 2

    return total_error / float(len(points))

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i]['OPEN']
        y = points.iloc[i]['HIGH']
        
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    # print(f"m_gradient: {m_gradient}, b_gradient: {b_gradient}") 

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    
    return m, b


m = 0
b = 0
L = 0.01                                                                                #Learning Rate
epochs = 1000                                                                           #Epochs

for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch:{i}")
    m, b = gradient_descent(m, b, data, L)

print(m, b)

plt.scatter(data.OPEN, data.HIGH, color = "black")
plt.plot(data['OPEN'], [m * x + b for x in data['OPEN']], color="red")
plt.xlabel('Open Prices')
plt.ylabel('High Prices')
plt.title('Open vs High Prices with Linear Regression Line')
plt.show()