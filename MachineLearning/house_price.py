import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import LinearRegression from scikit-learn module
from sklearn.linear_model import LinearRegression

size = np.array([500,800,1000,1200,1500]).reshape(-1,1)
price = np.array([100000,150000,200000,240000,300000])

model = LinearRegression()
model.fit(size,price)

new_size = np.array([[2000]])
predicted_price = model.predict(new_size)
print(predicted_price[0])

plt.scatter(size,price,color="blue")
plt.plot(size,model.predict(size),color="red")
plt.xlabel("SQFT")
plt.ylabel("COST")
plt.title("FIRST AI EXAMPLE")
plt.show()