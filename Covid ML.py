# Example Ml File
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

table = pd.read_csv("daily.csv")

X = table.Recovered.values
Y = table.Confirmed.values

plt.scatter(X, Y)
plt.show()
# Reshaping to 2D Array
X = X.reshape(len(X), 1)
Y = Y.reshape(len(Y), 1)


model = LinearRegression()
